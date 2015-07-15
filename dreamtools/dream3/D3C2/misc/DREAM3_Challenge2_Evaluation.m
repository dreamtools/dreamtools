function [norm_sq_error, pval] = DREAM3_Challenge2_Evaluation(testfile, goldfile, pdffile)
%
% This function evaluates the accuracy of a prediction compared 
% to a gold standard.
% 
% Usage: [norm_sq_error, pval] = DREAM3_Challenge2_Evaluation(testfile, goldfile, pdffile)
%
% INPUTS:
% 	testfile:	the file containing the predictions to be evaluated
%	goldfile:	the gold standard
%	pdffile:	the precomputed probability density
%
% OUTPUTS: 
%	nurm_sq_error:	the number of correct predictions
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


%% Read the probability density function that we computed (empirically) elsewhere
%% NOTE: This loads: X, Y, and C, where C is a constant that scales the pdf to the histogram
temp = load(pdffile);
X = temp.X;
Y = temp.Y;

%% read and parse files
[G, g_cell_type, g_stimulus, g_inhibitor, g_prediction_time, g_col_names] = read_challenge2_file(goldfile);
[T, cell_type, stimulus, inhibitor, prediction_time, col_names] = read_challenge2_file(testfile);

%% perform calculations
norm_sq_error = performance_score(G,T);
pval = probability(X,Y,norm_sq_error);

%% %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%% helper functions

function [A, cell_type, stimulus, inhibitor, prediction_time, col_names] = read_challenge2_file(file)
	d = importdata(file);
	%% these cols are fixed
	cell_type = d.textdata(2:end,1);
	stimulus = d.textdata(2:end,2);
	inhibitor = d.textdata(2:end,3);
	prediction_time = d.data(:,1);
	%% these col names correspond to the data matrix
	col_names = d.textdata(1,5:end);	% first row
	A = d.data(:,2:end);
end

function score = performance_score(G,A)
	ACC = 300;			% accuracy of the dector (lower limit of detection)
	GAMMA = 0.08;		% coeff of variation (gamma) mostly due to biological error
	[m n] = size(G);
	N = m*n;
	k = 1:N;
	g = G(k);
	a = A(k);
	numer = (a-g).^2;
	denom = ACC^2 + (GAMMA * g).^2;
	score = sum(numer./denom);
end

function P = probability(X,Y,x)
	dx = X(2)-X(1);
	P = sum( double(X<=x) .* Y * dx );
end


end
