#!/usr/bin/perl -w
## Raquel Norel (rnorel@us.ibm.com) 01/2015

#validate format of predictions for DREAM9.5 Olfactory Prediciton Challenge (sub challenge 1)
#not using gold standard here, hardcode or build needed info

use strict;
use Cwd qw(abs_path cwd);


## command line arguments
if (@ARGV != 3) {
    print "\nUSAGE:perl $0  <input file to validate> <output file> <flag L for Leaderboard or F for final submission>  \n\n";
    print "Format validation for DREAM9.5 Olfactory Prediction Sub Challenge 1\n";
    print "example: perl $0  my_prediction.txt errors.txt L\n";
    exit;
}


##PARAMETERS
my @header = ('#oID','individual','descriptor','value');#just in case, since values for different columns are quite different
my $DATA_POINTS = 71001;  # number of entries to get
my $Ncols = 4; # #oID	descriptor	value	sigma

#global variables
my %oIDs = ();
my %descriptors = ();
my %individuals = ();
my $dir = cwd();



#prediction file
my $file = $ARGV[0]; #input file, predictions
my $out_fn = "$dir/$ARGV[1]"; #output file, results from validaiton script
my $phase = $ARGV[2]; #use F for Final scoring and L for Leaderboard
if (($phase ne 'F') && ($phase ne 'L')){
    die "phase has to be either L or F not $phase. Bye...\n"; 
}
print STDERR "reading $file\n";

#generate  expected ids
my ($ref_val) = generate_ids($phase);
my %val = %$ref_val;

my $lines;
{
     open my $fh, "<", $file or die $!;
    local $/; # enable localized slurp mode
     $lines = <$fh>;
    close $fh;
}

my @all = split(/[\r\n]+/,$lines);  #Mac, Unix and DOS files
my $valid_data_lines=0; #how many valid data lines have been seen
my $check_header_flag=0;
my $errors = ''; #keep all errors to be reported to user
#while (<IN>) {
my $ln=1; 
foreach (@all){
#print STDERR "processing $_";
 my $line = $_;
	if ($line =~ /^\s*$/) {next;}	## skip blank lines
	
	#need to check for columns number before other check to avoid warning if less columns than expected
	my @tmp = split ("\t", $line); #separating line by comma, separate only once for all the tests
	$tmp[2] =~ s/\s//g; #remove spaces; detected on CHEMICAL
	my $n_cols = scalar @tmp; #number of columns
	if (!check_column_number($n_cols,$ln)){last;} #correct number of columns?	
	if (/^#/) {   ## check header, assume is 1st line
	    $check_header_flag++ ; #header detected
	    for (my $i=0; $i< scalar(@header); $i++){
		if ($tmp[$i] ne $header[$i]) {
		    $errors .= "\n".'ERROR in the header ';
		    my $tmpi = $i + 1;
		    $errors .= "Column $tmpi is $tmp[$i] and should be $header[$i]. Error at input line # $ln.\n";
		    last;
		}
	    }
	}
        else{
            if (!check_format_labels($tmp[0],$tmp[1],$tmp[2],$ln)){last;} #correct "labels", is it repeated?
            if (!check_format_cols4($tmp[3],$ln)){last;} #correct format of col 4; nuemeric betwwen 0 and 100
	    $valid_data_lines++;
	}
	$ln++;
}

if ($check_header_flag != 1) { $errors .=  "We didn't detect the correct header in the prediction file.\n";}
#error reporting
   open (FH, "> $out_fn") or die "cannot open $out_fn (why? $!)  \n";  

     if (($errors eq '' ) && ($valid_data_lines == $DATA_POINTS)) {print FH "OK\nValid data file\n";} #all good; still need to check for header count
     elsif (($errors eq '' ) && ($valid_data_lines < $DATA_POINTS)){
	check_missing(); #only check for missing prediction if no other errors are found, since quiting at 1st error
	print FH "NOT_OK\nYou have the following error(s): $errors\n";
	print FH "Please see the template file and  resubmit the updated file.\n";
     } 
    else {
              
	      print FH "NOT_OK\nYou have the following error(s): $errors\n";
	      print FH "Please see the template file and resubmit the updated file.\n";
	}

  close FH;

###########subroutines##############
#check id combinations with no predictions
sub check_missing{
     foreach my $k1 (sort keys %oIDs){
	for (my $i=1; $i<50; $i++){
	    foreach my $k2 (sort keys %descriptors){
		if ( $val{$k1}{$i}{$k2} < 0){ $errors .= "Missing predictions for $k1 $i $k2 entry\n";}
	    }
	}
     }
  return(1);
}


sub check_format_labels{ # checking the ID has not been used twice, and the name is correct
  my ($oid, $ind, $des, $ln) = @_;
  my $flag =1; #so far so good
if (!defined($oIDs{$oid})) { $errors .= "$oid is not a valid odor ID. Error at input line # $ln.\n"; return(0);} #failed test
if (!defined($descriptors{$des})) { $errors .= "$des is not a valid odor descriptor. Error at input line # $ln.\n"; return(0);} #failed test
if (!defined($individuals{$ind})) { $errors .= "$ind is not a valid individual id. Error at input line # $ln.\n"; return(0);} #failed test

  if($val{$oid}{$ind}{$des} == -1){
    $val{$oid}{$ind}{$des} = 1;
    }
  else {$errors .= "$oid, $ind with $des is a  duplicated entry. Error at input line # $ln.\n"; return(0);};  #failed test
   return(1);
}


 sub check_format_cols4{ #is numeric? is it between 0 and 100?
  my ($val,$ln) = @_;
 # if (( $val =~ /^([+-]?)(?=\d|\.\d)\d*(\.\d*)?([Ee]([+-]?\d+))?$/) && ($val >= 0) && ($val <= 1) || ($val == 1) || ($val==0)){
  if (( $val =~ /^([+]?)(?=\d|\.\d)\d*(\.\d*)?([Ee]([+-]?\d+))?$/) && ($val <= 100)){ #force to be positive
       return(1);
   } #test ok;
   #test failed 
  $errors .= "Value must be a positive float number, less or equal to 100. Got $val, which is incorrect.\nError at input line # $ln.\n";
   return(0);#failed test  
}
 

#since I don;t read the gold standard, I need to generate the expected full set if IDs on the prediction file, to check against it
sub generate_ids{
    my ($phase) = @_;
    my @Ldescriptors = qw(ACID AMMONIA/URINOUS BAKERY BURNT CHEMICAL COLD DECAYED FISH FLOWER FRUIT GARLIC GRASS INTENSITY/STRENGTH MUSKY SOUR SPICES SWEATY SWEET VALENCE/PLEASANTNESS WARM WOOD);
    my @LoIDs;
    if ($phase eq 'F'){
	@LoIDs = qw(1031 10857465 10886 11567 12020 12265 12377 1549025 15654 16537 17898 180 18467 21363 251531 262 264 2733294 27440 3102 31219 31276 31283 323 3314 440917 5281167 5281168 5318599);
	my @tmp1  = qw(5352837 5364231 5371102 5862 5962 60998 61523 62089 62351 62465 6274 6322 637758 6506 6544 6561 6669 702 7092 7137 7302 7476 750 753 7559);
	my @tmp2 = qw(7657 7770 7793 7797 8025 8049 8094 8419 8438 8468 853433 8815 8878 9012 962);
	push (@LoIDs, @tmp1);
	push (@LoIDs, @tmp2);
    }
    elsif ($phase eq 'L'){
	@LoIDs = qw(1030	1060	10722	11124	11419	12206	12348	12748	13187	13204	13216	13436	14328	1549778	1550470	15606	16220109	22386	24020	243	24473	2682	31210);
	my @tmp1  = qw(31266	33032	454	520108	5352539	5355850	5363233	5367698	61024	6114390	61151	61155	61177	61252	6137	61771	62572	638024	6386	641256	679	6826	6989);
	my @tmp2  = qw(7047	7409	7601	7632	778574	7792	7820	7826	8038	8048	8051	8078	8137	8159	8163	8175	8180	8205	8294	8452	8467	8615	9024);

	
	push (@LoIDs, @tmp1);
	push (@LoIDs, @tmp2);
    }
    my $No = scalar (@LoIDs); #print "there are $No elements in oIDs\n";
    my $Nd = scalar(@Ldescriptors); #print "there are $Nd descriptors\n";
    my %val = ();
    my %sigma = ();
    
    #convinient to have as hash as well for ease of checking
    for (my $i=0; $i<$No; $i++){
        $oIDs{$LoIDs[$i]} = 1;
	#print ".$LoIDs[$i].\n";
    }
    for (my $i=0; $i<$Nd; $i++){
        $descriptors{$Ldescriptors[$i]} = 1;
	#print ".$Ldescriptors[$i].\n";
    }
    for (my $i=1; $i<50; $i++){
	$individuals{$i} = 1;
    }
    

    for (my $i=0; $i<$No; $i++){
	for (my $k=1; $k<50; $k++){
	    for (my $j=0; $j<$Nd;$j++){
		$val{$LoIDs[$i]}{$k}{$Ldescriptors[$j]} = -1;
	    }
	}	
    }
    #return(\%val,\%sigma); #it is enough to check for one of the values, since I alrwady check for number of columns
    return(\%val); 
}

#check that the number of columns per line is ok
sub check_column_number{
  my ($n_cols, $ln) = @_;
	if ($n_cols != $Ncols) {
	   $errors .=  "Please note that the numbers of expected columns is $Ncols not $n_cols. Error at input line # $ln.\n";
	   return(0);#failed test
	}
	return(1); #test ok 
}



