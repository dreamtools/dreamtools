

%scoring in 4 metrics the D6C3

tmp = importdata ('dream6_expred_predictions_0.txt');
GS = tmp.data;
pt=21; %number of participants
prom=53; %number of promotors

%reading data
for i=1:pt %number of teams
  tmp  = importdata( [ 'dream6_expred_predictions_'  num2str(i) '.txt']); %%read YOUR FILE	
  tmp2 = tmp.data;
  data(:,i)=tmp2;
  indx(:,i)=tiedrank(tmp2);
end;

fid = fopen('team_scores_TRx2.txt','wt');
fprintf (fid,'team\tPearson\tSpearman\tchi_sq\trank_sq\n');

ings=tiedrank(GS);


for t=1:pt %number of teams
  p = corr(GS,data(:,t)); %Pearson
  s = corr(GS,data(:,t), 'type','Spearman'); %Spearman
  
  % chi-square
  chi=0;
  for i=1:prom
     n1 = (data(i,t) - GS(i));
	 s2 =0;
	 for j=1:pt
	    d1 = data(i,j) - GS(i);
		s2 = s2 + d1*d1;
	 end
	 s2 = s2/pt;
     chi = chi + (n1*n1)/s2;
  end;
  
  %rank square
   
  r2 = 0;
  for i=1:prom
     rn1 = indx(i,t) - ings(i);
	 rs2 =0;
	 for j=1:pt
	    rd1 = indx(i,j) - ings(i);
		rs2 = rs2 + rd1*rd1;
	 end
	 
	 rs2 = rs2/pt;
     
	 r2 = r2 + (rn1*rn1)/rs2;
  end;
  
  
    
  fprintf (fid,'%d\t%7.5f\t%7.5f\t%7.5f\t%7.5f\n',t,p,s,chi,r2);
end
 fclose(fid);

