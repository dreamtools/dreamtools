#!/usr/bin/perl -w

#Raquel Norel
#rnorel@us.ibm.com
#January 2015
#scoring script for DREAM9.5 Olfaction Prediction challenge Q1
 
use strict;
use Cwd qw(abs_path cwd);

### command line arguments
if (@ARGV != 3) {
    print "\nUSAGE: $0  <file to evaluate> <output file>  <gold standard file>  \n\n";
    print "Predictions evaluation for DREAM9.5 Olfaction Prediction  challenge Q2\n";
    print "example: perl $0  my_prediction.txt my_score.txt GS_Q2.txt \n";
    exit;
}


####   MAIN ####

my $in_fn = $ARGV[0];
my $out_fn = $ARGV[1];
my $gs_fn =  $ARGV[2];              #"$dir/Data/GS_Q1.txt";
my @sd = qw(0.119307474	0.126471379	0.026512975	0.119494682	0.11490659	0.02808499); #to be used to compuet Z-scores for final score

print STDOUT "Script ASSUMES that all the files to be evaluated passed the validation script\n";
#read Gold Standard
my %descriptor = (); #keep descriptor names for looping later
my %oID = (); #keep odor IDs for looping
my %indiv = (); #need to remove

my $ref_gs_val;
my $ref_gs_sigma;

($ref_gs_val,$ref_gs_sigma) = &read_GS($gs_fn);

#     print "$ref_gs_val";
    my ($ref_pred_val, $ref_pred_sigma) = &read_prediction("$in_fn");
    my ($ref_pccs_val, $ref_pccs_sigma) = &get_pccs($ref_pred_val, $ref_gs_val,$ref_pred_sigma, $ref_gs_sigma); 
    my ($intensity_val,$valence_val,$avg_19_val,$intensity_sigma,$valence_sigma,$avg_19_sigma) = &compute_scores($ref_pccs_val, $ref_pccs_sigma);
    my $Zscore = ($intensity_val/$sd[0] + $valence_val/$sd[1] + $avg_19_val/$sd[2] + $intensity_sigma/$sd[3] + $valence_sigma/$sd[4] + $avg_19_sigma/$sd[5])/6;
    open (FH, "> $out_fn") or die "cannot open $out_fn (why? $!)\n"; 
	print FH "intensity val \t valence val \t 19 other val \tintensity sigma \t valence sigma \t 19 other sigma\tavg of Z-scores\n";
	print FH "$intensity_val\t$valence_val\t$avg_19_val\t$intensity_sigma\t$valence_sigma\t$avg_19_sigma\t$Zscore\n";
    close FH;

######   SUBROUTINES   #######
sub compute_scores{
    my ($ref_pccs_val,$ref_pccs_sigma) = @_;
    my %pccs_val = %$ref_pccs_val;
    my %pccs_sigma = %$ref_pccs_sigma;
    my $sum_all_val=0;
    my $sum_all_sigma=0;
    my %avg = ();
    #average all individuals for a given descriptor
     foreach my $k1 (sort keys %descriptor){
	#keep addition of all cases, then substract 2 cases with more weigth
	$sum_all_val += ($pccs_val{$k1});
	$sum_all_sigma += ($pccs_sigma{$k1});
     }
     my $intensity_val = $pccs_val{'INTENSITY/STRENGTH'};
     my $intensity_sigma = $pccs_sigma{'INTENSITY/STRENGTH'};
     my $valence_val = $pccs_val{'VALENCE/PLEASANTNESS'};
     my $valence_sigma = $pccs_sigma{'VALENCE/PLEASANTNESS'};
     my $sum_19_val = $sum_all_val - $intensity_val - $valence_val;
    my $sum_19_sigma = $sum_all_sigma - $intensity_sigma - $valence_sigma;
    #print "INT $avg_intensity VAL $avg_valence sumALL $sum_all sum19 $sum_19 avg19 $avg_19\n";    
     return($intensity_val,$valence_val,$sum_19_val/19,$intensity_sigma,$valence_sigma,$sum_19_sigma/19)
     
}

#get the 21 x 49 PCC, one per "column" per for a given prediction
#depending on the flag substract or not average for that column
sub get_pccs{
    my ($ref_pred_val, $ref_gs_val,$ref_pred_sigma, $ref_gs_sigma) = @_;
    
    my %pred_val = %$ref_pred_val;
    my %pred_sigma = %$ref_pred_sigma;
    my %GS_val = %$ref_gs_val;
    my %GS_sigma = %$ref_gs_sigma;
    
    my %pccs_val = ();
    my %pccs_sigma = ();
    
    foreach my $k1 (sort keys %descriptor){
	    my @vec1_val = (); #push values fomr GS
	    my @vec2_val = (); #push values form predictions
	    my @vec1_sigma = (); #push values fomr GS
	    my @vec2_sigma = (); #push values form predictions
	    foreach my $k2 (sort keys %oID){
		 push(@vec1_val,$GS_val{$k2}{$k1});
		 push(@vec2_val,$pred_val{$k2}{$k1});
		 push(@vec1_sigma,$GS_sigma{$k2}{$k1});
		 push(@vec2_sigma,$pred_sigma{$k2}{$k1});
	    }
	 # my $correl_val =  MyUtil::pearson(\@vec1_val,\@vec2_val); #copy function to make this script stand alone!
	 # my $correl_sigma =  MyUtil::pearson(\@vec1_sigma,\@vec2_sigma);
	   my $correl_val =  pearson(\@vec1_val,\@vec2_val); #copy function to make this script stand alone!
	   my $correl_sigma =  pearson(\@vec1_sigma,\@vec2_sigma);
	   $pccs_val{$k1} = $correl_val;
	    $pccs_sigma{$k1} = $correl_sigma;
	}
    return(\%pccs_val,\%pccs_sigma);
    
}

#from GS hash get a matrix with averages to use later
#oID	individual	descriptor	value
#180	1	INTENSITY/STRENGTH	0
sub get_avg_GS{
    my ($ref_gs) = @_;
    my %GS = %$ref_gs;
    my %AVG_oID = ();
    foreach my $k1 (sort keys %descriptor){
	foreach my $k2 (sort keys %indiv){
	    my $c=0;
	    my $sum=0;
	    foreach my $k3 (sort keys %oID){
		if ($GS{$k3}{$k2}{$k1} >=0){
		    $sum += $GS{$k3}{$k2}{$k1};
		    $c++;
		}
	    }
	    $AVG_oID{$k1}{$k2} = $sum/$c;
	   # print "TESTING descriptor: $k1  individuoe: $k2  sum $sum and ctn = $c\n";exit;
	}
    }
    
    return(\%AVG_oID);
}

#read the prediciton file
sub read_prediction{
  my ($fn) = @_;

   my %pred_val = ();
   my %pred_sigma = (); 
    my $lines;
{
     open my $fh, "<", $fn or die $!;
    local $/; # enable localized slurp mode
     $lines = <$fh>;
    close $fh;
}
    my @all = split(/[\r\n]+/,$lines);  #Mac, Unix and DOS files
    foreach (@all){
       # print "processing $_\n";
        #chomp;
       # s/\s+$//; #instead of chomp
        if (/^#/) {next;} #skip header
        my @tmp = split "\t";
	$tmp[1] =~ s/\s//g; #remove spaces #found extra spaces on CHEMICAL on GS
        if ((scalar @tmp) != 4) {die "check format of prediction in $fn. Bye\n";}
	$pred_val{$tmp[0]}{$tmp[1]} = $tmp[2];
	$pred_sigma{$tmp[0]}{$tmp[1]} = $tmp[3];
      }

    return(\%pred_val,\%pred_sigma); #return reference to hash with predictions
}

#read the gold standard
#keep 3 indeces for reference, keep all in one hash
#use -1 insted of NaN as a flag
#data is as  #oID	individual	descriptor	value
sub read_GS{
  my ($fn) = @_;
  my %gs_val = ();
  my %gs_sigma = ();
    open (FH, "$fn") or die "cannot open $fn (why? $!)   (from read_GS)\n";
      while (<FH>){
        #chomp;
        s/\s+$//; #instead of chomp
        if (/^#/) {next;} #skip header
	#$_ =~ s/^\s+|\s+$//g; #OJO
	#trim($_);
	#$_ =~ s/\s//g; #remove spaces
        my @tmp = split "\t";
	$tmp[1] =~ s/\s//g; #remove spaces #found extra spaces on CHEMICAL on GS
    #print join(" + \t",@tmp),"\n";#exit;
        if ((scalar @tmp) != 4) {die "check format of GS in $fn (just read $_). Bye\n";}
	#just flagging who exists
	$oID{$tmp[0]}= 1;
	$descriptor{$tmp[1]} = 1;
	$gs_val{$tmp[0]}{$tmp[1]} = $tmp[2];
	$gs_sigma{$tmp[0]}{$tmp[1]} = $tmp[3];
      }
    close FH;
    return(\%gs_val,\%gs_sigma); #return reference to hashes
}

###what follows is taken from  MyUtil.pl 
#compute Pearson correlation between 2 vectors
#pass the reference to each vector
sub pearson{
   my ($ref_a,$ref_b) = @_;
   my @a = @$ref_a;
   my @b = @$ref_b;
   if (scalar(@a) != scalar (@b)) {die "vectors need to be of the same size for Pearosn. Bye\n";}
   
   my $sig_b = diff_sum($ref_b);
   my $sig_a = diff_sum($ref_a);
   my $mean_a = &average($ref_a);
   my $mean_b = &average($ref_b);

   my $N = scalar(@a);

   my $sum=0;
   for (my $i=0; $i<$N; $i++){
      my $dife_a = $a[$i] - $mean_a;
      my $dife_b = $b[$i] - $mean_b;
      $sum += $dife_a*$dife_b; 
   }
   my $den = $sig_a * $sig_b;
   my $p = 0;
   if ($den != 0){
      $p = $sum/($sig_a * $sig_b);
   }
   return($p);
}


sub average{
        my($data) = @_;
        if (not @$data) {
                die("Empty array\n");
        }
        my $total = 0;
        foreach (@$data) {
         if (! defined $_){die "OJO empty cell from AVERAGE (not defined  ) \n";}
                $total += $_;
        }
        my $average = $total / @$data;
        return $average;
}

sub diff_sum{
   my ($ref_a) = @_;
   my @a = @$ref_a;
   
   my $N = scalar(@a);
   my $mean_a = &average($ref_a);
   my $sum=0;
   for (my $i=0; $i<$N; $i++){
      my $dife = $a[$i] - $mean_a;
      $sum += $dife*$dife; 
   }
   return (sqrt($sum));
   
}


