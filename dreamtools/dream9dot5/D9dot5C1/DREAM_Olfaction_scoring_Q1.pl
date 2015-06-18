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
    print "Predictions evaluation for DREAM9.5 Olfaction Prediction  challenge\n";
    print "example: perl $0  my_prediction.txt my_score.txt GS_Q1.txt \n";
    exit;
}


####   MAIN ####
my $in_fn = $ARGV[0];
my $out_fn = $ARGV[1];
my $gs_fn =  $ARGV[2]; 
my @sd = qw(0.018728962	0.01759068	0.00424504); #to be used to compuet Z-scores for final score

print STDOUT "Script ASSUMES that all the files to be evaluated passed the validation script\n";
#read Gold Standard
my %descriptor = (); #keep descriptor names for looping later
my %oID = (); #keep odor IDs for looping
my %indiv = (); #individuals go from 1 to 49; still keep for completness or in case they change ID later

my $ref_gs;
$ref_gs = &read_GS($gs_fn);

my $ref_avg;
$ref_avg = &get_avg_GS($ref_gs); #compute the average of the values per "column" to be substracted when doing Pearson-in at least one of the versions
my ($ref_pred) = &read_prediction("$in_fn");
my $ref_pccs = &get_pccs($ref_pred, $ref_gs,0,'fake'); #pass 0 to use all values as they are, use 1 to substract AVG for column
my ($avg_intensity,$avg_valence,$avg_19) = &compute_scores($ref_pccs);
my $Zscore = ($avg_intensity/$sd[0] + $avg_valence/$sd[1] + $avg_19/$sd[2])/3;
open (FH, "> $out_fn") or die "cannot open $out_fn (why? $!)\n"; 
    print FH "avg intensity\tavg valence\tavg 19 other\tavg of Z-scores\n";
    print FH "$avg_intensity\t$avg_valence\t$avg_19\t$Zscore\n";
close FH;

######   SUBROUTINES   #######
sub compute_scores{
    my ($ref_pccs) = @_;
    my %pccs = %$ref_pccs;
    my $sum_all=0;
    my %avg = ();
    #average all individuals for a given descriptor
     foreach my $k1 (sort keys %descriptor){
	my $sum=0;
	my $c = 0;
	foreach my $k2 (sort keys %indiv){
	    $sum += $pccs{$k1}{$k2};
	    $c++;
	}
	$avg{$k1} = $sum/$c;
	#keep addition of all cases, then substract 2 cases with more weigth
	$sum_all += ($sum/$c);
     }
     my $avg_intensity = $avg{'INTENSITY/STRENGTH'};
     my $avg_valence = $avg{'VALENCE/PLEASANTNESS'};
     my $sum_19 = $sum_all - $avg_intensity - $avg_valence;
     my $avg_19 = $sum_19/19;
   #  print "INT $avg_intensity VAL $avg_valence sumALL $sum_all sum19 $sum_19 avg19 $avg_19\n";    
     return ($avg_intensity,$avg_valence,$avg_19);
     
}

#get the 21 x 49 PCC, one per "column" per for a given prediction
#depending on the flag substract or not average for that column
sub get_pccs{
    my ($ref_pred, $ref_gs, $flag, $ref_avg_oIDs) = @_;
    
    my %pred = %$ref_pred;
    my %GS = %$ref_gs;
    
    my %pccs = ();
    if ($flag==0){ #duplicate code, but ask only once about flag
    foreach my $k1 (sort keys %descriptor){
	foreach my $k2 (sort keys %indiv){
	    my @vec1 = (); #push values fomr GS
	    my @vec2 = (); #push values form predictions
	    foreach my $k3 (sort keys %oID){
		if ($GS{$k3}{$k2}{$k1} >=0){
		 push(@vec1,$GS{$k3}{$k2}{$k1});
		 push(@vec2,$pred{$k3}{$k2}{$k1});
		# print "$k1\t$k2\t$k3\t$GS{$k3}{$k2}{$k1}\t$pred{$k3}{$k2}{$k1}\n";
		}
	    }
	  # my $correl =  MyUtil::pearson(\@vec1,\@vec2); #copied form MyUtil to make this script stand alone
	  my $correl =  pearson(\@vec1,\@vec2);
	   $pccs{$k1}{$k2} = $correl;
	}
    }
    }
    else{ #flag =1
	my %take = %$ref_avg_oIDs;
	 foreach my $k1 (sort keys %descriptor){
	foreach my $k2 (sort keys %indiv){
	    my @vec1 = (); #push values fomr GS
	    my @vec2 = (); #push values form predictions
	    foreach my $k3 (sort keys %oID){
		if ($GS{$k3}{$k2}{$k1} >=0){
		    my $tk = $take{$k1}{$k2};
		 push(@vec1,($GS{$k3}{$k2}{$k1} - $tk));
		 push(@vec2,($pred{$k3}{$k2}{$k1} - $tk));
		 print "restando $tk para $k1\t$k2\t$k3\n";
	     #print "$k1\t$k2\t$k3\t$GS{$k3}{$k2}{$k1}\t$pred{$k3}{$k2}{$k1}\n";
		}
	    }
	   my $correl =  MyUtil::pearson(\@vec1,\@vec2);
	   $pccs{$k1}{$k2} = $correl;
	}
    }
	exit;
	
    }
    return(\%pccs);
    
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

   my %pred = (); 
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
	$tmp[2] =~ s/\s//g; #remove spaces #found extra spaces on CHEMICAL on GS
        if ((scalar @tmp) != 4) {die "check format of prediction in $fn. Bye\n";}
	$pred{$tmp[0]}{$tmp[1]}{$tmp[2]} = $tmp[3];
      }

    return(\%pred); #return reference to hash with predictions
}

#read the gold standard
#keep 3 indeces for reference, keep all in one hash
#use -1 insted of NaN as a flag
#data is as  #oID	individual	descriptor	value
sub read_GS{
  my ($fn) = @_;
  my %GS = ();
    open (FH, "$fn") or die "cannot open $fn (why? $!)   (from read_GS)\n";
      while (<FH>){
        #chomp;
        s/\s+$//; #instead of chomp
        if (/^#/) {next;} #skip header
	#$_ =~ s/^\s+|\s+$//g; #OJO
	#trim($_);
	#$_ =~ s/\s//g; #remove spaces
        my @tmp = split "\t";
	$tmp[2] =~ s/\s//g; #remove spaces #found extra spaces on CHEMICAL on GS
	# print join(" + \t",@tmp),"\n";#exit;
        if ((scalar @tmp) != 4) {die "check format of GS in $fn (just read $_). Bye\n";}
	#just flagging who exists
	$oID{$tmp[0]}= 1;
	$indiv{$tmp[1]} =1;
	$descriptor{$tmp[2]} = 1;
	if ($tmp[3] eq 'NaN') {$GS{$tmp[0]}{$tmp[1]}{$tmp[2]} = -1;}
	else {$GS{$tmp[0]}{$tmp[1]}{$tmp[2]} = $tmp[3];}
      }
    close FH;
    return(\%GS); #return reference to hash
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




