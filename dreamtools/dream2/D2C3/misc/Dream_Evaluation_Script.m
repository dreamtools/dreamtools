function DreamEvaluationScript(testfile, goldfile)
% The function DreamEvaluationScript evaluates the accuracy of a prediction compared to
% a gold standard
% 
% Usage: DreamEvaluationScript(testfile, goldfile)
%
% DreamEvaluationScript calcuates a precision and ROC values for a given prediction 
% (testfile) compared to a gold standard (goldfile) and generates appropiate plots. 
% The input file (testfile) name holds the information on which goldstandard 
% should be used for comparison. fid3 is a file point to file for logging 
% purposes it is used to collect results from different executions of the script 
% in one file. 
% 
% The file name of testfile is checked for "_UNDIRECTED" and "BCL6targets"
% to identify data that relates to challenge 1 and undirected predictions
% for those pose special cases in the analysis.
% 
% All further information about the actual calculations can be found elsewhere.
%
%
% The algorithm was developed by Gustavo Stolovitzky and implemented by
% Bernd Jagla, Columbia University (baj2107_A_T_columbia.edu). All questions/suggestions should be
% directed to both, Gustavo and Bernd.
%
% Gustavo A. Stolovitzky, Ph.D.
% Adj. Assoc Prof of Biomed Informatics, Columbia Univ
% Mngr, Func Genomics & Sys Biology, IBM  Research
% P.O.Box 218                                  Office :  (914) 945-1292
% Yorktown Heights, NY 10598  Fax     :  (914) 945-4217
% http://www.research.ibm.com/people/g/gustavo
% http://domino.research.ibm.com/comm/research_projects.nsf/pages/fungen.index.html 
%
% Bernd Jagla, Ph.D.
% Assoc. Rsch. Scientist
% Joint Centers for Systems Biology
% Columbia University
% Irving Cancer Res Ctr
% 1130 St Nicholas Avenue 8th Floor
% United States

% Read and understand file name in order to check for challenge 1 or
% directed/undirected
[pathstr, name, ext] = fileparts(testfile);
testfile = name;
undirected = regexp(testfile, '_UNDIRECTED');
bcl6 = regexp(testfile, 'BCL6targets');

% read in data
% Gold standard
maxN = 10000000;
fid1 = fopen(goldfile, 'r');
if fid1 < 1
    filecore
    goldfile
    error(['Problem reading goldstandard: ' goldfile]);
end
if isempty(bcl6)
    gold=textscan(fid1,'%s%s%f', maxN);
    if (isempty(undirected))
        gold{1} = strcat('A',gold{1},'___',gold{2});
    else
        %gold{1} = mkName(gold{1},gold{2});
        gold{1} = strcat(gold{1},gold{2});
    end
    gold{2} = gold{3};
else
    gold=textscan(fid1,'%s%f', maxN);
    gold{1} = strcat('A',gold{1});
end
fclose(fid1);

for i=1:length(gold{1})
    goldstruct.(char(gold{1}(i))) = i;
end

%test/sample data
fid2 = fopen([pathstr testfile ext], 'r');
if isempty(bcl6)
    test=textscan(fid2,'%s%s%f', maxN);
    if (isempty(undirected))
        % test{1} can be a number so lets add some character before
        test{1} = strcat('A', test{1}, '___', test{2});
    else
        %test{1} = mkName(test{1},test{2});
        test{1} = strcat(test{1},test{2});
    end
    test{2} = test{3};
else
    test=textscan(fid2,'%s%f',maxN);
    test{1} = strcat('A', test{1});
end
fclose(fid2);

% remove all entries from test that are not in the goldstandard
keepme = [];
j = 1;
for i=1:length(test{1})
    if isfield(goldstruct,test{1}(i))
        keepme(j) = i;
        j = j + 1;
    end
end
test{1} = test{1}(keepme);
test{2} = test{2}(keepme);

% Analysis
% initialization

k=0;
Ak=0;
TPk=0;
FPk=0;
P = sum(gold{2});
N = length(gold{1}) - P;
T = length(gold{1});
L = length(test{1});

% do the calculations
if ~ isempty(test{1})
    while (k < L)
        k = k + 1;
        if mod(k,1000) == 0
            disp(sprintf('%d of %d',k,L));
        end
        p = goldstruct.(char(test{1}(k)));
        %this should not happen
        if length(p) >1
            error(char(test{1}(kk)) , ' not found');
        end
        if gold{2}(p) == 1
            TPk = TPk + 1;
            if(k==1)        
                delta=1/P;  
            else            
                delta=(1-FPk*log(k/(k-1)))/P;
            end            
            Ak = Ak + delta; 
        elseif gold{2}(p) == 0
            FPk = FPk + 1;
        else
            % for challange 5 ignore unknown interactions
            disp(['couldnot find ' char(test{1}(k))]);
        end
        rec(k) = TPk/P;
        prec(k) = TPk/k;
        tpr(k) = rec(k);
        fpr(k) = FPk/N;
    end
end

TPL=TPk;
if L < T
    rh = (P-TPL)/(T-L); 
else
    rh = 0;
end

if L>0
    recL = rec(L);
else
    recL = 0;
end
while TPk < P
    k = k + 1;
    TPk = TPk + 1;
    rec(k) = TPk/P;
    if ((rec(k)-recL)*P + L * rh) ~= 0
        prec(k) = rh * P * rec(k)/((rec(k)-recL)*P + L * rh);
    else
        prec(k) = 0;
    end
    tpr(k) = rec(k);
    FPk = TPk * (1-prec(k))/prec(k);
    fpr(k) = FPk/N;
end
AL = Ak;
if ~isnan(rh) && rh ~= 0  && L ~= 0 
    AUC = AL + rh * (1-recL) + rh * (recL - L * rh / P) * log((L * rh + P * (1-recL) )/(L *rh));
elseif(L==0)
    AUC = P/T;           
else
    AUC = Ak;
end

%Integrate area under ROC

lc = fpr(1) * tpr(1) /2;
for n=1:L+P-TPL-1
    lc = lc + (fpr(n+1)+fpr(n)) * (tpr(n+1)-tpr(n)) / 2;
end

AUROC = 1 - lc;

% specific precision values
TrueP = [1 2 5 20 100 500]; 
prec0 = zeros(6,1);
for i=1:length(TrueP)
    if(TrueP(i)<=P)
        rec0(i)=TrueP(i)/P;
        j=find(rec == rec0(i));
        j=min(j); %In case there is more than 1 precision values for rec(i)
        prec0(i)=prec(j);
    end
end
first = 0;
k =1;
while k < L
    if prec(k) > 0
        first = prec(k);
        k = L;
    end
    k=k+1;
end

% Output
figPrecRec = createfigurePrecRec(prec,rec);
print (figPrecRec, '-djpeg', [pathstr name '_precRec.jpg']);
delete( figPrecRec);

figROC = createfigureROC(tpr, fpr);
print (figROC, '-djpeg', [pathstr name '_ROC.jpg']);
delete (figROC);

fid = printoutNew([pathstr name '_evaluation.txt']);

% print to analysis file for user to see
fprintf(fid, '\n-------------------------PLOTS-----------------------------\n');
printout(fid, 'PrecPlot', [pathstr name '_precRec.jpg']);
printout(fid, 'ROCPlot',[pathstr name '_ROC.jpg']);
fprintf(fid, '\n------------Area Under the PR and ROC Curves---------------\n');
printout(fid, 'Precision-Recall',AUC);
printout(fid, 'ROC curve',AUROC);
fprintf(fid, '\n------------Precision at n-th correct prediction-----------\n');
if(prec0(1)>0)
    printout(fid, 'n=1',prec0(1));
else
    printout(fid, 'n=1','NA');
end

if(prec0(2)>0)
    printout(fid, 'n=2',prec0(2));
else
    printout(fid, 'n=2','NA');
end

if(prec0(3)>0)
    printout(fid, 'n=5',prec0(3));
else
    printout(fid, 'n=5','NA');
end

if(prec0(4)>0)
    printout(fid, 'n=20',prec0(4));
else
    printout(fid, 'n=20','NA');
end

if(prec0(5)>0)
    printout(fid, 'n=100',prec0(5));
else
    printout(fid, 'n=100','NA');
end


if(prec0(6)>0)
    printout(fid, 'n=500',prec0(6));
else
    printout(fid, 'n=500','NA');
end

printoutEnd(fid);

end



%% create figures functions
% createfigurePrecRec
% createfigureROC

function figure1 = createfigurePrecRec(rec1, prec1)
%CREATEFIGURE(PREC1,REC1)
%  PREC1:  vector of x data
%  REC1:  vector of y data

% Create figure
figure1 = figure;

% Create axes
axes('Parent',figure1);
% Uncomment the following line to preserve the X-limits of the axes
xlim([0 1]);
ylim([0 1]);
box('on');
hold('all');

% Create plot
plot(prec1,rec1,'LineWidth',2);

% Create ylabel
ylabel({'Precision'},'fontsize',16);

% Create xlabel
xlabel({'Recall'},'fontsize',16);

% Create title
title({'Precision vs. Recall'},'fontsize',20);
end

function figure1 = createfigureROC(rec1, prec1)
%CREATEFIGURE(PREC1,REC1)
%  PREC1:  vector of x data
%  REC1:  vector of y data

% Create figure
figure1 = figure;

% Create axes
axes('Parent',figure1);
% Uncomment the following line to preserve the X-limits of the axes
xlim([0 1]);
ylim([0 1]);
box('on');
hold('all');

% Create plot
plot(prec1,rec1,'LineWidth',2);

% Create ylabel
ylabel({'True Positive Rate'},'fontsize',16);

% Create xlabel
xlabel({'False Positive Rate'},'fontsize',16);

% Create title
title({'ROC'},'fontsize',20);
end

%% Utility functions for printing out XML formated files
% printcloseAnalysis 
% printoutNew
% printopenAnalysis
% printout
% printoutEnd


function fid = printoutNew(fpname)
fid = fopen(fpname, 'w');
if fid <1
    error ('error creating analysis output file');
end
end


function printout(fid, tag, content)
if isnumeric(content)
    if isa(content, 'integer')
        fprintf(fid, '%-15s %d\n',tag,content);
    else
        fprintf(fid, '%-15s %f\n',tag,content);
    end
else
    fprintf(fid, '%-15s %s\n',tag,content);
end
end

function printoutEnd(fid)
fclose(fid);
end
