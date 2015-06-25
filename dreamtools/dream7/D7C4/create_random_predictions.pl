###################################################################
#
# Usage: 
# > perl create_random_predictions.pl
#
# Output:
# the ouput of this script will be a set of randomly generated predictions
# that will be used to create the null distributions.  Set the variable 
# $number_of_random for the number of random predictions to be generated.  
# The NCI-DREAM Challenge was set to 10000.
#
# This script was created by Jim Costello to score the NCI-DREAM
# drug sensitivity challenge.  Please contact me at jccostel@bu.edu
# for further questions.                               
#
#################################################################

######
# global variables
my $outdir = "random_predictions/";
my $number_of_random = 100;

######
# read in the list of test cell lines.  This list will be
# randomly shuffled and insterted in the the training data
# to produce a set of random predictions
my @test = ();
open(FILE, "data/DREAM7_DrugSensitivity1_test_data.txt") || die;
while(<FILE>) {
    chomp;
    my ($cellLine, @vals) = split(/\t/, $_);
    next if $cellLine eq 'CellLine';
    push(@test, $cellLine);
}
close FILE;

# an array that will have all 53 cell lines (18 test and 35 training)
my @lines = @test;

######
# The training data is the same for all random predictions because the 
# GI50 value have been already given to participants.   The challenge
# was to insert the predited 18 cell lines into the list of 35 training cell
# lines. 
my @drugs = ();
my %train = ();
open(FILE, "data/DREAM7_DrugSensitivity1_Drug_Response_Training.txt") || die;
while(<FILE>) {
    chomp;
    my ($cellLine, @vals) = split(/\t/, $_);
    if ($cellLine eq 'CellLine') { # header line that contains the drugs ids
	@drugs = @vals;
    } else { # all cell lines rows
	push(@lines, $cellLine);
	for(my $i=0; $i<=$#vals; $i++) {
	    if ($vals[$i] eq 'NA') { # set all NA values to 0
		$vals[$i] = 0;
		push(@{$train{$drugs[$i]}{$vals[$i]}}, $cellLine);
	    } else {
		push(@{$train{$drugs[$i]}{$vals[$i]}}, $cellLine);
	    }
	}
    }    
}
close FILE;


######
# start the loop for creating $number_of_random  random predictions
for(my $i=1; $i<=$number_of_random; $i++) {

# loop through all the drugs, shuffle the test cell lines and insert them 
# randomly into the ranked training cell lines. 
    my %rank = ();
    foreach my $d(@drugs) {
	fy_shuffle(\@test);
	fy_shuffle(\@test);
	fy_shuffle(\@test);

	my $rank_ctr = 1; # the running rank of the cell line, will end at 53
	my $index_test = 0; # the index of the test cell line being inserted into the training data

	foreach my $v(sort {$b<=>$a} keys %{$train{$d}}) {
	    foreach my $c(@{$train{$d}{$v}}) {
		if (rand(1) < .5 && $index_test < 18) { # randomly insert a test cell line
		    $rank{$test[$index_test]}{$d} = $rank_ctr;
		    $rank_ctr++;
		    $index_test++;
		}
		$rank{$c}{$d} = $rank_ctr;
		$rank_ctr++;
	    }
	}

	for(my $i=$index_test; $i<18; $i++) { # place any remaining test cell lines at the end 
	    $rank{$test[$i]}{$d} = $rank_ctr;
	    $rank_ctr++;
	}	
    }
    

    ######
    # print the output of the ith set of random predictions.
    my $outfile = $outdir . "sc1_random_" . $i . ".txt";

    open(OUT, ">$outfile") || die;
    print OUT "DrugAnonID";
    foreach my $d(@drugs) { # first print the header row
	print OUT ",$d";
    }
    print OUT "\n";

    foreach my $c(@lines) { # print the ranks for all 53 cell lines
	print OUT $c;
	foreach my $d(@drugs) {
	    print OUT ",$rank{$c}{$d}";
	}
	print OUT "\n";
    }

    print STDERR "Random prediction number $i has been written\n" if (($i %1000) == 0);
}

print STDERR "Success, there should be $number_of_random random prediction in $outdir\n";
exit;




######
# fisher yate shuffle subroutine
sub fy_shuffle {
    my $array = shift;
    my $i;
    for ($i = @$array; --$i; ) {
        my $j = int rand ($i+1);
        next if $i == $j;
        @$array[$i,$j] = @$array[$j,$i];
    }
}
