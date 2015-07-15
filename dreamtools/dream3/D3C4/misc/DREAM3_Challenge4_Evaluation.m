function [AUC AUROC P_AUC P_AUROC] = DREAM3_Challenge4_Evaluation(testfile, goldfile, pdffile)
%
% This function evaluates the accuracy of a prediction compared 
% to a gold standard.
% 
% Usage: [AUC AUROC P_AUC P_AUROC] = 
%		DREAM3_Challenge4_Evaluation(testfile, goldfile, pdffile)
%
% INPUTS:
%	testfile:	the file containing the predictions to be evaluated
%	goldfile: 	the file containing the gold standard
%	pdffile:  	the file containing a precomputed probability density
%			for computing p-values.
%
% OUTPUTS: 
%	AUC:		area under the precision-recall curve (also called AUPR)
%	AUROC:		area under the ROC curve
%	P_AUC:		p-value for AUC
%	P_AUROC:	p-value for AUROC
% All further information about the actual calculations can be found elsewhere.

% The algorithm was developed by Gustavo Stolovitzky and implemented by
% Bernd Jagla, Columbia University (baj2107_A_T_columbia.edu). 
% All questions/suggestions should be directed to both, Gustavo and Bernd.
%
% Gustavo A. Stolovitzky, Ph.D.
% Adj. Assoc Prof of Biomed Informatics, Columbia Univ
% Mngr, Func Genomics & Sys Biology, IBM  Research
% P.O.Box 218 					Office :  (914) 945-1292
% Yorktown Heights, NY 10598 	Fax     :  (914) 945-4217
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
%
% Robert Prill, Ph.D.
% Postdoctoral Researcher
% Computational Biology Center, IBM Research
% P.O.Box 218
% Yorktown Heights, NY 10598 	
% Office :  914-945-1377
% http://domino.research.ibm.com/researchpeople/rjprill.index.html
%

% read goldfile
maxN = 10000000;
fid1 = fopen(goldfile, 'r');
gold=textscan(fid1,'%s%s%f', maxN);
gold{1} = strcat('A',gold{1},'___',gold{2});
gold{2} = gold{3};
fclose(fid1);

for i=1:length(gold{1})
    goldstruct.(char(gold{1}(i))) = i;
end

% read testfile
fid2 = fopen(testfile, 'r');
test=textscan(fid2,'%s%s%f', maxN);
% test{1} can be a number so lets add some character before
test{1} = strcat('A', test{1}, '___', test{2});
test{2} = test{3};
fclose(fid2);

% remove all entries from test that are not in the goldstandard
% (e.g., self-edges)
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

% Initialization
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

%% assume random accuracy for remainder of links
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


%% %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%% compute p-values

temp = load(pdffile);
x_auroc = temp.x_auroc;
y_auroc = temp.y_auroc;
x_aupr = temp.x_aupr;
y_aupr = temp.y_aupr;

P_AUC   = probability(x_aupr, y_aupr, AUC);
P_AUROC = probability(x_auroc, y_auroc, AUROC);


%% %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%% helper functions

% P(X>=x)
function P = probability(X,Y,x)
	dx = X(2)-X(1);
	P = sum( double(X>=x) .* Y * dx );
end

end
