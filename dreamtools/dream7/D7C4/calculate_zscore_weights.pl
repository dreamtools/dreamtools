################################################################
#
# Usage: 
# > perl calculate_zscore_weights.pl
#
# You must have run the script "create_random_predictions.pl"
# to populate the random_predictions directory with random predictions.
#
# Output:
# the ouput of this script is a tab-delimited text file that 
# lists contains the zscores (and normalized zscores) comparing the
# gold standard test data to the empirical null distributions.  These
# values are treated as weights for drugs as not all drugs have equal
# signal for predictive purposes.
#
# This script was created by Jim Costello to score the NCI-DREAM
# drug sensitivity challenge.  Please contact me at jccostel@bu.edu
# for further questions.              
#
#################################################################

use Games::Go::Erf qw(erf);

######
# define some global variables
my $rand_dir = "random_predictions/";
my $sdfile = "data/DREAM7_DrugSensitivity1_Pooled_SD.txt";
my $testdatafile = "data/DREAM7_DrugSensitivity1_test_data.txt";
my $outfile = "data/DREAM7_DrugSensitivity1_drug_zscores.txt";

######
# The standard deviation for the anonymized drugs are contained
# within this file.  These information will be used later on.
my %pooledSD = ();
open(FILE, "$sdfile") || die;
while(<FILE>) {
    chomp;
    next if $_ =~ /^\#/;
    my ($anonId, $sd) = split(/\t/, $_);
    next if $anonId eq 'AnonID';
    $pooledSD{$anonId} = $sd;
}
close FILE;
print STDERR "The standard deviations for " . keys(%pooledSD) . " drugs have been read\n";

######
# The test data is parsed and used for scoring
my %gi50 = ();
my @drugs = ();
open(FILE, "$testdatafile") || die;
while(<FILE>) {
    chomp;
    my ($cellLine, @vals) = split(/\t/, $_);
    if ($cellLine eq 'CellLine') {
	@drugs = @vals;
    } else {
        # read in all the values and set the NA values to 0
	for(my $i=0; $i<=$#vals; $i++) {
	    if ($vals[$i] eq 'NA') {
		$gi50{$cellLine}{$drugs[$i]} = 0;
	    } else {
		$gi50{$cellLine}{$drugs[$i]} = $vals[$i];
	    }
	}
    }
}
close FILE;
my $n = $#drugs + 1;
print STDERR keys(%gi50) . " cell lines and $n drugs have been read in from the test data\n";


######
# This file is the ranked training and test data together.  All values have been 
# experimentally tested. This represents the gold standard.
my @drugs = ();
my %preds = ();
open(FILE, "data/DREAM7_DrugSensitivity1_Train_Test_Ranked.csv") || die "Please enter a file to score\n";
while(<FILE>) {
    chomp;
    my ($cellLine, @vals) = split(/\,/, $_);
    if ($cellLine eq 'DrugAnonID') {
        @drugs = @vals;
    } else {
        for(my $i=0; $i<=$#vals; $i++) {
            $preds{$cellLine}{$drugs[$i]} = $vals[$i];
        }
    }    
}
close FILE;

######
# first score all the random predictions.  Read in all the randomly generated
# predictions in the random_predictions directory. 
my %randomscores = ();
my $ct = 0;
opendir(DIR, "$rand_dir") || die;
while(my $file = readdir(DIR)) {
    next if $file !~ /random/;

    $ct++;
    print "$ct random predictions scored\n" if (($ct %100) == 0);

    my %randpreds = ();
    my @randdrugs = ();
    $file = $rand_dir . $file;
    open(FILE, "$file") || die "random file not found; $file\n";
    while(<FILE>) {
	chomp;
	my ($cellLine, @vals) = split(/\,/, $_);
	if ($cellLine eq 'DrugAnonID') {
	    @randdrugs = @vals;
	} else {
	    for(my $i=0; $i<=$#vals; $i++) {
		$randpreds{$cellLine}{$drugs[$i]} = $vals[$i];
	    }
	}    
    }
    close FILE;

    # loop through all the drugs and score them individually using the probablisitic c-index
    foreach my $drug (@randdrugs) {    

        # select the cell lines to score, for a given drug, there will be a variable number of cell lines
	my @cell_lines = ();
	foreach my $line(keys %randpreds) {
	    next if $gi50{$line}{$drug} ==0;
	    push(@cell_lines, $line);
	}

	my $score = calculate_prob_cindex(\@cell_lines,$drug,\%gi50,\%randpreds,\%pooledSD);
	push(@{$randomscores{$drug}}, $score);
    } 
}
closedir DIR;

######
# from all of the random scores, calculated the mean and standard deviation
my %random_mean = get_random_mean(\%randomscores);
my %random_sd = get_random_sd(\%randomscores, \%random_mean);


#####
# score the gold standard data and then compare this value to the null distribution for each drug.
# calculate the zscore.
my $max_zscore = 0;
my %zscore_temp = ();
foreach my $drug (@drugs) {    
    # select the cell lines to score, for a given drug, there will be a variable number of cell lines
    my @cell_lines = ();
    foreach my $line(keys %gi50) {
        next if $gi50{$line}{$drug} ==0;
	push(@cell_lines, $line);
    }

    if ($random_sd{$drug} != 0) { # some drugs have no standard deviation because the measured values for that drug are all the same
	my $score = calculate_prob_cindex(\@cell_lines,$drug,\%gi50,\%preds,\%pooledSD);
	my $z = ($score - $random_mean{$drug}) / $random_sd{$drug};
	$max_zscore = $z if $z > $max_zscore;
	$zscore_temp{$drug} = $z;
    } else {
	$zscore_temp{$drug} = 0;
    }
} 



#####
# print the zscores and the normalized zscore (zscore/max zscore)
open(OUT, ">$outfile") || die;
print OUT "# file contains the precomputed z-scores and normalized zscores\n";
print OUT "# for all 31 drugs.  These precomputed values are based on a\n";
print OUT "# set of 10,000 random predictions of the test data.  The final\n";
print OUT "# row contains the mean and variance of the overall score, which\n";
print OUT "# is used to calculate the signficance of the overall score for\n";
print OUT "# a set of predictions\n";
my %zscore_gold = ();
while(my ($k, $v) = each(%zscore_temp)) {
    $zscore_gold{$k} = $v/$max_zscore;
    print OUT "$k\t$v\t$zscore_gold{$k}\n";
}

#####
# now that we have calculated the weights, we have to rescore all the random predictions using the
# weights to calculate the overall weighted average probabilistic c-index.
my @overallscores = ();
my $ct = 0;
opendir(DIR, "$rand_dir") || die;
while(my $file = readdir(DIR)) {
    next if $file !~ /random/;

    $ct++;
    print "$ct random predictions scored for the overall score\n" if (($ct %100) == 0);

    my %randpreds = ();
    my @randdrugs = ();
    $file = $rand_dir . $file;
    open(FILE, "$file") || die "random file not found; $file\n";
    while(<FILE>) {
	chomp;
	my ($cellLine, @vals) = split(/\,/, $_);
	if ($cellLine eq 'DrugAnonID') {
	    @randdrugs = @vals;
	} else {
	    for(my $i=0; $i<=$#vals; $i++) {
		$randpreds{$cellLine}{$drugs[$i]} = $vals[$i];
	    }
	}    
    }
    close FILE;

    my $randweightsum = 0; # running sum
    my $randweightctr = 0; # running counter
    foreach my $drug (@randdrugs) {    
        # select the cell lines to score, for a given drug, there will be a variable number of cell lines
	my @cell_lines = ();
	foreach my $line(keys %randpreds) {
	    next if $gi50{$line}{$drug} ==0;
	    push(@cell_lines, $line);
	}

        # incorporate the weights, which is the normalzied zscore
	my $score = calculate_prob_cindex(\@cell_lines,$drug,\%gi50,\%randpreds,\%pooledSD);
	my $weight = $score * $zscore_gold{$drug};
	$randweightsum += $weight;
	$randweightctr += $zscore_gold{$drug};
    } 

    # the weighted average is simply the summation of the score times the weights divided by the summation of the weights
    my $randws = sprintf("%.5f", ($randweightsum/$randweightctr));
    push(@overallscores, $randws);
}
closedir DIR;

#####
# calculate the mean and variance of the overall score and print it out
my $sum = 0;
foreach my $v(@overallscores) {
    $sum += $v;
}
my $overallmean = $sum/($#overallscores + 1);

my $sum = 0;
foreach my $v(@overallscores) {
    $sum += ($v - $overallmean) * ($v - $overallmean);
}
my $overallvar = $sum/$#overallscores;
print OUT "Overall\t$overallmean\t$overallvar\n";

close OUT;
exit;


#######
# subroutine that calculates the probabilistic c-index
sub calculate_prob_cindex {
    my $cell_line_ref = shift;
    my $drugname = shift;
    my $gi50_ref = shift;
    my $pred_ref = shift;
    my $pooledSD_ref = shift;

    my $sum = 0; # keeps the running sum 
    my %done = (); # keeps track of if we have seen the cell line pair.  This is needed to account for the cell lines
                   # that have the same values.  They would be counted twice if they are not accounted for


    for(my $i=0; $i<=$#{$cell_line_ref}; $i++) {
        my $test_val1 = $gi50_ref->{$cell_line_ref->[$i]}{$drugname}; # concentration of cell line i from the test data
        my $pred_val1 = $pred_ref->{$cell_line_ref->[$i]}{$drugname}; # rank of cell line i from the predictions
        for(my $j=0; $j<=$#{$cell_line_ref}; $j++) {
            next if $j == $i;
            my $test_val2 = $gi50_ref->{$cell_line_ref->[$j]}{$drugname}; # concentration of cell line j from the test data
            my $pred_val2 = $pred_ref->{$cell_line_ref->[$j]}{$drugname}; # rank of cell line j from the predictions
            if ($test_val1 >= $test_val2 && $pred_val1 < $pred_val2) { # the concordance case
                next if defined($done{$j}{$i});
                my $cdf = .5 * (erf(($test_val1 - $test_val2)/(sqrt(2*($pooledSD_ref->{$drugname} * $pooledSD_ref->{$drugname})))) + 1);
                $sum += $cdf; # the running sum will add a value between .5 and 1
                $done{$i}{$j}++;
            } elsif ($test_val1 >= $test_val2 && $pred_val1 > $pred_val2) { # the discordance case
                next if defined($done{$j}{$i});
                my $cdf = 1 - (.5 * (erf(($test_val1 - $test_val2)/(sqrt(2*($pooledSD_ref->{$drugname} * $pooledSD_ref->{$drugname})))) + 1));
                $sum += $cdf; # the running sum will add a value between 0 and 1
                $done{$i}{$j}++;
            } 
        }
    }
    
    # in the end, all cell line pairs will be tested once or, (n * n-1)/2  
    my $n = (($#{$cell_line_ref} + 1) * $#{$cell_line_ref}) / 2;
    return ($sum/$n);
}




#######
# subroutine to calculate the mean of the random predictions per drug
sub get_random_mean {
    my $ref = shift;
    my %temp = %{$ref};

    my %ret = ();
    foreach my $drug(keys %temp) {
	my $sum = 0;
	foreach my $v(@{$temp{$drug}}) {
	    $sum += $v;
	}
	my $ave = $sum / ($#{$temp{$drug}} + 1);
	$ret{$drug} = $ave;
    }
    return %ret;
}


#######
# subroutine to calculate the mean of the random predictions per drug
sub get_random_sd {
    my $ref = shift;
    my $mean_ref = shift;
    my %temp = %{$ref};

    my %ret = ();
    foreach my $drug(keys %temp) {
	my $sum = 0;
	foreach my $v(@{$temp{$drug}}) {
	    $sum += ($v - $mean_ref->{$drug})*($v - $mean_ref->{$drug});
	}
	my $sd = sqrt($sum / $#{$temp{$drug}});
	$ret{$drug} = $sd;
    }
    return %ret;
}
