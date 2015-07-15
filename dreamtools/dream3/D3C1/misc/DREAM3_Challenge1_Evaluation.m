function [num_correct pval] = DREAM3_Challenge1_Evaluation(testfile, goldfile, pdffile)
%
% This function evaluates the accuracy of a prediction compared 
% to a gold standard.
% 
% Usage: [num_correct pval] = ...
%	DREAM3_Challenge1_Evaluation(testfile, goldfile, pdffile)
%
% INPUTS:
% 	testfile:	the file containing the predictions to be evaluated
%	goldfile:	the gold standard
%	pdffile:	the precomputed probability density
%
% OUTPUTS: 
%	num_correct:	the number of correct predictions
%	pval:		p-value
%
% All further information about the actual calculations can be found elsewhere.

% Gustavo A. Stolovitzky, Ph.D.
% Adj. Assoc Prof of Biomed Informatics, Columbia Univ
% Mngr, Func Genomics & Sys Biology, IBM  Research
% P.O.Box 218 					Office :  (914) 945-1292
% Yorktown Heights, NY 10598 	Fax     :  (914) 945-4217
% http://www.research.ibm.com/people/g/gustavo
% http://domino.research.ibm.com/comm/research_projects.nsf/pages/fungen.index.html 
%
% Robert Prill, Ph.D.
% Postdoctoral Researcher
% Computational Biology Center, IBM Research
% P.O.Box 218
% Yorktown Heights, NY 10598 	
% Office :  914-945-1377
% http://domino.research.ibm.com/researchpeople/rjprill.index.html
%


T = read_challenge1_file(testfile);
G = read_challenge1_file(goldfile);

%% load the probability density (really a prob mass function for this challenge)
temp = load(pdffile);
X = temp.X;
Y = temp.Y;

%% add-up the correct predictions
idx = find(G);
num_correct = sum(T(idx));

pval = probability(X,Y,num_correct);

%% %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%% helper functions

function A = read_challenge1_file(file)
	d = importdata(file);
	A = d.data;
	[m,n] = size(A);
	if m~=4 || n~=7
		error('Problem parsing file')
		%% Make sure there are no blank lines between the header and the data
	end
end

function P = probability(X,Y,x)
	dx = X(2)-X(1);
	P = sum( double(X>=x) .* Y * dx );
end

end
