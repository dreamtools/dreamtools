
% load contestant results
y = dir('aggregate');
for i =3:length(y);

    printf('%s\n', y(i).name);
    [nt1 s1 nt2 s2 nt3] = textread(['aggregate/' y(i).name  '/dream7_netparinf_networktopo_model_' int2str(2) '_' y(i).name '.txt'], '%d %s %d %s %d ');

    % load gold standard
    [nt_1 s_1 nt_2 s_2 nt_3] = textread(['goldstandard/model' int2str(2) '_topology_answer.txt'], '%d %s %d %s %d ');


 %network topology
  d=0;w=0;int=0;
    for j=1:3; for k=1:3;

    if nt_1(j)==nt1(k) & nt_2(j)==nt2(k) &  strcmp(s_1(j),s1(k)) & nt_2(j)>0 & nt_1(j)>0

        d = d + 6 ;   nt2(k)=0; int(w+1)=k; w=w+1;


    if nt_1(j)==nt1(k) & nt_3(j)==nt3(k) &  strcmp(s_2(j),s2(k)) & nt_3(j)>0 & nt_1(j)>0

        d = d + 6 ;  nt3(k)=0; int(w+1)=k; w=w+1;

    end;end;end;end;

if int>0 nt1(int)=0; end;

nt1
s1
nt2

clear lgs rgs lp rp igs ip

lgs(1:3,1)=nt_1;
rgs(1:3,1)=nt_2;
rgs(4:6,1)=nt_3;
lp(1:3,1)=nt1;
rp(1:3,1)=nt2;
rp(4:6,1)=nt3;
igs(1:3,1)=s_1;
igs(4:6,1)=s_2;
ip(1:3,1)=s1;
ip(4:6,1)=s2;

iz=find(rp);
rp=rp(iz);
ip=ip(iz);

rp
ip

[rp,iu]=unique(rp);
ip=ip(iu);
lp=unique(lp);




    for k=1:3, for j=1:length(lp);

        if lgs(k)==lp(j) & lgs(k)>0, d=d+1;
            printf('HERE d=d+1\n');
            printf('%s' , y(i).name);
        end;
    end;end;

rp
rgs
igs
ip

    for k=1:6, for j=1:length(rp);

        if rgs(k)==rp(j) & rgs(k)>0, d=d+1;if strcmp(igs(k),ip(j)); d=d+1;
        
        
        
        end;
        end;
    end;end;

printf('####')

end;


