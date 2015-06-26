
import os
from dreamtools.core.challenge import Challenge


class D3C4(Challenge):
    """A class dedicated to D3C4 challenge


    ::

        from dreamtools import D3C4
        s = D3C4()
        filename = s.download_template() 
        s.score(filename) 

    Data and templates are downloaded from Synapse. You must have a login.

    """
    def __init__(self):
        """.. rubric:: constructor

        """
        super(D3C4, self).__init__('D3C4')
        self._path2data = os.path.split(os.path.abspath(__file__))[0]
        self._init()
        self.sub_challenges = []

    def _init(self):
        # should download files from synapse if required.
        pass

    def score(self, prediction_file):
        raise NotImplementedError

    def download_template(self):
        # should return full path to a template file
        pass

    def load_gs(self):
        """ % read goldfile
        maxN = 10000000;
        fid1 = fopen(goldfile, 'r');
        gold=textscan(fid1,'%s%s%f', maxN);
        gold{1} = strcat('A',gold{1},'___',gold{2});
        gold{2} = gold{3};
        fclose(fid1);

        for i=1:length(gold{1})
            goldstruct.(char(gold{1}(i))) = i;
        end
        """
        pass

    def load_test(self):
        """% read testfile
        fid2 = fopen(testfile, 'r');
        test=textscan(fid2,'%s%s%f', maxN);
        % test{1} can be a number so lets add some character before
        test{1} = strcat('A', test{1}, '___', test{2});
        test{2} = test{3};
        fclose(fid2);
        """
        pass


"""
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
    k = 0
    Ak = 0
    TPk = 0
    FPk = 0

    P = sum(gold{2})
    N = length(gold{1}) - P
    T = length(gold{1})
    L = length(test{1})

    % do the calculations
    while k < L
        k = k + 1
        #if mod(k, 1000) == 0
        #    disp(sprintf('%d of %d',k,L))
        #end
        p = goldstruct.(char(test{1}(k)))
        %this should not happen
        if len(p) >1:
            error(char(test{1}(kk)) , ' not found');
        end

        if gold{2}[p] == 1:
            TPk = TPk + 1.

            if k == 1:
                delta = 1. / P  
            else:            
                delta = (1. - FPk*np.log(k/(k-1.))) / P
            
            Ak = Ak + delta

        elif gold{2}[p] == 0
            FPk = FPk + 1.
        else:
            #  for challange 5 ignore unknown interactions
            print('could not find ' + 'test{1}(k)')
        
        rec.append(TPk/float(P))
        prec.append(TPk/float(k))
        tpr.append(rec[k-1])
        fpr.append(FPk/float(N))
    

    # assume random accuracy for remainder of links
    TPL = TPk
    if L < T:
        rh = (P-TPL) / float(T-L)
    else:
        rh = 0.


    if L>0
        recL = rec[L-1]
    else
        recL = 0;

    while TPk < P:
        k = k + 1
        TPk = TPk + 1.
        rec.append(TPk / float(P))
        if ((rec[k-1]-recL)*P + L * rh) != 0:
            prec.append( rh * P * rec[k-1]/((rec[k-1]-recL)*P + L * rh))
        else:
            prec.append(0)
        
        tpr.append(rec[k-1])
        FPk = TPk * (1-prec[k-1])/prec[k-1];
        fpr(k) = FPk/float(N)

    AL = Ak
    #if ~isnan(rh) && rh ~= 0  && L ~= 0 
    if rh != 0  and L != 0:
        AUC = AL + rh * (1.-recL) + rh * (recL - L * rh / P) 
                    * np.log((L * rh + P * (1-recL) )/(L *rh))
    elif L == 0:
        AUC = P / float(T)
    else
        AUC = Ak
    

    # Integrate area under ROC
    lc = fpr[0] * tpr[0] /2.
    for n in range(1,int(L+P-TPL-1 + 1)):
        lc = lc + ( fpr[n] + fpr[n-1]) * (tpr[n]-tpr[n-1]) / 2.
    AUROC = 1. - lc


        import scipy.io
        temp = scipy.io.loadmat(pdffile)
        x_auroc = temp.x_auroc
        y_auroc = temp.y_auroc
        x_aupr = temp.x_aupr
        y_aupr = temp.y_aupr

        P_AUC   = self.probability(x_aupr, y_aupr, AUC);
        P_AUROC = self.probability(x_auroc, y_auroc, AUROC);

        return AUC, AUROC, prec, rec, tpr, fpr, P_AUROC, p_AUC

    """

    def probability(self, X, Y, x):
        dx = X[2] - X[1]
        P = sum( np.double(self.X >= x) * Y * dx )
        return P


