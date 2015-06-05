
% load contestant results
y = dir('aggregate');
distances = zeros(length(y)-3, 4);
pvalues = zeros(length(y)-3, 4);

for i =4:length(y);
    [xname prm1] = textread([ 'aggregate/' y(i).name '/dream7_netparinf_parameters_model_' int2str(1) '_' y(i).name '.txt'], '%s %f');
    [t p11 p12 p13] = textread([ 'aggregate/' y(i).name '/dream7_netparinf_timecourse_model_' int2str(1) '_' y(i).name '.txt'], '%f %f %f %f', 'headerlines',1);
    
    [xname prm2] = textread([ 'aggregate/' y(i).name '/dream7_netparinf_parameters_model_' int2str(2) '_' y(i).name '.txt'], '%s %f');
    [nt1 s1 nt2 s2 nt3] = textread(['aggregate/' y(i).name  '/dream7_netparinf_networktopo_model_' int2str(2) '_' y(i).name '.txt'], '%d %s %d %s %d ');
    
    % load gold standard
    [xname prm1_] = textread(['gs/model' int2str(1) '_parameters_answer.txt'], '%s %f');
    [t p11_ p12_ p13_] = textread(['gs/model' int2str(1) '_prediction_answer.txt'], '%f %f %f %f', 'headerlines',1);
    
    [xname prm2_] = textread(['gs/model' int2str(2) '_parameters_answer.txt'], '%s %f');
      
    [nt_1 s_1 nt_2 s_2 nt_3] = textread(['gs/model' int2str(2) '_topology_answer.txt'], '%d %s %d %s %d ');
      
 %prmb and p11b p12b p13b, have all the contestants submissions 
 
 prmb(:,i-2)=prm1; p11b(:,i-2)=p11; p12b(:,i-2)=p12;p13b(:,i-2)=p13;
 
 %model1     
 
 %distance for parameters
    distances(i-2,1) = sum((log10(prm1 ./ prm1_)).^2) / length(prm1_); 
    
    
 %distance for predictions
 
   d1(i-2,1)= sum(sum(((p11(11:40) - p11_(11:40)).^2) ./ (0.01 + 0.04*p11_(11:40).^2))) / 90;
   d1(i-2,2)= sum(sum(((p12(11:40) - p12_(11:40)).^2) ./ (0.01 + 0.04*p12_(11:40).^2))) / 90;
   d1(i-2,3)= sum(sum(((p13(11:40) - p13_(11:40)).^2) ./ (0.01 + 0.04*p13_(11:40).^2))) / 90;
   
    distances(i-2,2) = d1(i-2,1)+d1(i-2,2)+d1(i-2,3);

end;    
%Distribution Relative Null hypothesis; 
    
for i=1:10000
    
    for k=1:45
        
    prrm1(k,i)=prmb(k,randi([1 9],1,1)); %we only use the best 9 teams to randomize
    
    end;
    
    
    for k=1:41
        
    pr1(k,i)=p11b(k,randi([1 9],1,1)); %we only use the best 9 teams to randomize
    
    pr2(k,i)=p12b(k,randi([1 9],1,1));
    
    pr3(k,i)=p13b(k,randi([1 9],1,1));
    
    
   
    end;
    
    



rdist(i,1) = sum((log10(prrm1(:,i) ./ prm1_)).^2) / length(prm1_);


rdist(i,2) = sum(sum(((pr1(11:41,i) - p11_(11:41)).^2) ./ (0.01 + 0.04*p11_(11:41).^2))) / 90 +sum(sum(((pr2(11:41,i) - p12_(11:41)).^2) ./ (0.01 + 0.04*p12_(11:41).^2))) / 90+sum(sum(((pr3(11:41,i) - p13_(11:41)).^2) ./ (0.01 + 0.04*p13_(11:41).^2))) / 90;

end;
 