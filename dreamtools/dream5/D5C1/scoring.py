"""


Gustavo A. Stolovitzky, Ph.D.
Robert Prill, Ph.D.

"""
import os
from dreamtools.core.challenge import Challenge
import pandas as pd
import numpy as np


class D5C1(Challenge):
    """A class dedicated to D5C1 challenge


    ::

        from dreamtools import D5C1
        s = D5C1()
        filename = s.download_template() 
        s.score(filename) 

    Data and templates are downloaded from Synapse. You must have a login.

    """
    def __init__(self):
        """.. rubric:: constructor

        """
        super(D5C1, self).__init__('D5C1')
        self._path2data = os.path.split(os.path.abspath(__file__))[0]
        self._init()
        self.sub_challenges = []

    def _init(self):
        # should download files from synapse if required.
        self._download_data('AUPR.mat', 'syn4560154')
        self._download_data('AUROC.mat', 'syn4560158')
        self._download_data('DREAM5_EAR_GoldStandard.tsv', 'syn4560182')
        self._download_data('DREAM5_EAR_myteam_Predictions.txt', 'syn4560167')

    def download_template(self):
        # should return full path to a template file
        return self.get_pathname('DREAM5_EAR_myteam_Predictions.txt')

    def download_goldstandard(self):
        # should return full path to a gold standard file
        return self.get_pathname('DREAM5_EAR_GoldStandard.tsv')

    def _load_proba(self):
        import scipy.io
        self.auroc = scipy.io.loadmat(self.get_pathname("AUROC.mat"))
        self.aupr = scipy.io.loadmat(self.get_pathname("AUPR.mat"))

    def score(self, filename):

        self._load_proba()
        prediction = pd.read_csv(filename, sep='[ \t]', engine='python', header=None)
        gold = pd.read_csv(self.download_goldstandard(), sep='[ \t]', 
                engine='python', header=None)
        prediction.columns = ['sequence', 'value']
        gold.columns = ['sequence', 'value']

        # merge the prediction and gold based on the sequence.
        data = pd.merge(prediction, gold, how='inner', on=['sequence'], 
                suffixes=['_pred', '_gold'])
        # sory by prediction
        data.sort(columns=['value_pred'], ascending=False, inplace=True)
        data.columns = ['Sequence', 'prediction_values', 'prediction']

        self.data = data

        from dreamtools.core.rocs import ROCDiscovery
        self.roc = ROCDiscovery(self.data['prediction'])
        self.roc.get_statistics()
        auroc = self.roc.compute_auc()
        aupr = self.roc.compute_aupr()


        P_AUPR = self._probability(self.aupr['X'][0], self.aupr['Y'][0], aupr)
        P_AUROC = self._probability(self.auroc['X'][0], self.auroc['Y'][0], auroc)

        # overall dream score
        #i#P = [ p_auroc p_aupr ];
        #o#verall_score = mean(-log10(P)')';

        score = np.mean(-np.log10([P_AUROC, P_AUPR]))

        return {'auroc':auroc, 'aupr':aupr, 'pval_aupr': P_AUPR, 'pval_auroc':P_AUROC,
                'score':score}


    def _probability(self, X, Y, x):
        dx = X[2] - X[1]
        return  sum( Y[X>=x] * dx )

"""
function [TPR FPR PREC REC L AUROC AUPR P_AUROC P_AUPR] = DREAM5_Challenge1_Evaluation(gold, discovery, pdf_aupr, pdf_auroc)

%% total, positive, negative, length
P = sum(gold);
N = sum(~gold);
T = P + N;
L = length(discovery);

if L < T
	disp('ERROR: Truncated Prediction List')
end

%% true positives (false positives) at depth k
TPk = cumsum(discovery);
FPk = cumsum(~discovery);

K = [1:T]';

%% metrics
TPR = TPk / P;
FPR = FPk / N;
REC = TPR;  %% same thing
PREC = TPk ./ K;

%% %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%% Integrate area under ROC using trapezoidal rule
%AUROC = 0;
%for i = 1:T-1
%    AUROC = AUROC + ( FPR(i+1) - FPR(i) ) * ( TPR(i+1) + TPR(i) ) / 2;
%end

%% faster built-in integration function
AUROC = trapz(FPR,TPR);

%% %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%% Integrate area under PR curve using (Stolovitzky et al. 2009)

%%% initialize the first value
%if positive_discovery(1)
%	A = 1/P;
%else
%	A = 0;
%end
%
%%% integrate up to L
%for k = 2:L
%	if positive_discovery(k)
%		A = A + 1/P * ( 1 - FPk(k-1) * log(k/(k-1)) );
%	end
%end
%
%%% the remainder of the list is monatonic, so use trapezoidal rule
%A = A + trapz(REC(L+1:end),PREC(L+1:end));
%
%%% finally, normalize by max possible value
%A = A / (1-1/P);
%
%AUPR = A;

%% built-in function
AUPR = trapz(REC,PREC) / (1-1/P);	%% normalized by max possible value.


%% %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%% calcaulate p-values for these metrics

X = pdf_aupr.X;
Y = pdf_aupr.Y;
P_AUPR = probability(X, Y, AUPR);

X = pdf_auroc.X;
Y = pdf_auroc.Y;
P_AUROC = probability(X, Y, AUROC);


%% %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%figure(1); clf
%pn = 2;
%pm = 2;
%pj = 0;
%
%pj = pj + 1; subplot(pn,pm,pj)
%plot(FPR(1:L),TPR(1:L),'r')
%hold on
%plot(FPR(L+1:end),TPR(L+1:end),'b')
%hold off
%xlabel('FPR')
%ylabel('TPR')
%hold on
%plot([0,1],[0,1],'k--')  %% diagonal
%hold off
%axis([0,1,0,1])
%
%pj = pj + 1; subplot(pn,pm,pj)
%plot(REC(1:L),PREC(1:L),'r')
%hold on
%plot(REC(L+1:end),PREC(L+1:end),'b')
%hold off
%xlabel('Recall')
%ylabel('Precision')
%axis([0,1,0,1])
function [sequences, values, discovery] = load_prediction_list(file)

d = importdata(file);
sequences = d.rowheaders;
values = d.data(:,1);
if size(d.data,2)>1
	discovery = d.data(:,2);
end

% P(X>=x)
function P = probability(X,Y,x)

dx = X(2)-X(1);
P = sum( double(X>=x) .* Y * dx );
% This script demonstrates how to call the function 
% DREAM5_Challenge1_Evaluation().
%
% Gustavo A. Stolovitzky, Ph.D.

clear all

pdf_auroc = load(pdffile_auroc);

%% calculate performance metrics
[tpr fpr prec rec L auroc aupr p_auroc p_aupr] = DREAM5_Challenge1_Evaluation(gold, prediction, pdf_aupr, pdf_auroc);

%% overall dream score
P = [ p_auroc p_aupr ];
overall_score = mean(-log10(P)')';

%% show
aupr
auroc
p_aupr
p_auroc
overall_score

%% %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%% write results to text file
outfile = '../OUTPUT_step2/results.txt';
fid = fopen(outfile, 'w');

fprintf(fid,'OVERALL_SCORE\n');
fprintf(fid,'%.3f\n\n',overall_score);

fprintf(fid,'AUPR\n');
fprintf(fid,'%.3f\n\n',aupr);

fprintf(fid,'AUROC\n');
fprintf(fid,'%.3f\n\n',auroc);

fprintf(fid, 'P_AUPR\n');
fprintf(fid,'%.3e\n\n',p_aupr);

fprintf(fid, 'P_AUROC\n');
fprintf(fid,'%.3e\n\n',p_auroc);


%% %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%% show plots
figure(1)
subplot(2,2,1)
plot(fpr,tpr)
title('ROC')
xlabel('FPR')
ylabel('TPR')
subplot(2,2,2)
plot(rec,prec)
title('P-R')
xlabel('Recall')
ylabel('Precision')
print('-dpdf','../OUTPUT_step2/ROC_PR')

"""
