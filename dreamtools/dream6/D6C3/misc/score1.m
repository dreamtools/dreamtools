
b=importdata('dream6_expred_predictions_0.txt');
d=b.data;

pt=21; %number of participants

%reading data
for i=1:pt %number of teams
  a  = importdata( [ 'dream6_expred_predictions_'  num2str(i) '.txt']); %%read YOUR FILE	
  rd(:,i) = a.data;
end;  
%for j=1:pt; % participant j
    
 %   p=randperm(53);
    
%for i=1:53; % number of entries
 %   rd(i,j)=d(p(i));   %randomize entry 
%end;
%end;


%DISTANCE SCORING

%PEARSON

for i=1:pt;

Cp(i)=(sum(rd(:,i).*d)-sum(rd(:,i))*sum(d)/53)/sqrt(sum((rd(:,i)-sum(rd(:,i))/53).^2)*sum((d-sum(d)/53).^2));

Cp2(i)= corr(d,rd(:,i)); %Pearson
  
end;

%CHI-SQUARE

for i=1:pt; 
    suma=0;
    for j=1:53;
        suma=suma+((rd(j,i)-d(j)).^2)/(sum((rd(j,:)-d(j)).^2)/pt);
    end;
    X2(i)=suma;
end;

%RANK SCORING

ix=tiedrank(d); 

%SPEARMAN

for j=1:pt;
ixe(:,j)=tiedrank(rd(:,j));
end;

for i=1:pt; 

Sp(i)= (sum(ixe(:,i).*ix)-sum(ixe(:,i))*sum(ix)/53)/sqrt(sum((ixe(:,i)-sum(ixe(:,i))/53).^2)*sum((ix-sum(ix)/53).^2));
Sp2(i)=corr(ix,ixe(:,i), 'type','Spearman'); %Spearman
end;

%RANK2

for i=1:pt; 
    suma=0;
    for j=1:53;
        
      suma=suma+((ixe(j,i)-ix(j)).^2)/(sum((ixe(j,:)-ix(j)).^2)/pt);
    end;
      R2(i)=suma;
end;

for j=1:pt;
    FS(j,1)=Cp(j);
    FS(j,2)=X2(j);
    FS(j,3)=Sp2(j);
    FS(j,4)=R2(j);
end;
    
    
    %Aggregate
    %sc i]=sort(ans,'descend')
    %for j=1:20 for k=1:53 agg(k,j)=mean(rd(k,ii(1:j))); end;end;
  
