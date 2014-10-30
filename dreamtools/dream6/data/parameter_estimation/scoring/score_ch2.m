function [distances pvalues score] = score_ch2(path_to_pred, path_to_gs, team_name)
% [distances pvalues score] = score_ch2(path_to_pred, path_to_gs, team_name)
% Scores predictions for DREAM6, Callenge 2. Outputs p-values and distances
% to the gold standard in the following order:
% 1. Parameters Model 1
% 2. Parameters Model 2
% 3. Parameters Model 3
% 4. TimeCourse Model 1
% 5. TimeCourse Model 2
% 6. TimeCourse Model 3
%
% Input:
% path_to_pred - path to the directory with prediction files
% path_to_gs - path to the directory with gold standard files
% team_name - the name of the team
%
% Output:
% distances - distances to gold standard
% pvalues - p-values for each individual distance
% score - final score calculated as -log(prod(pvalues))
%
% Note: Prediction files need to be in the same format as gold standard
% files. File names should follow this naming convention:
% dream6_parest_parameters_model_<i>_<team_name>.txt and
% dream6_parest_timecourse_model_<i>_<team_name>.txt


% Two gamma mixture model
pi = [0.4212 0.5788; ...
      0.3344 0.6656; ...
      0.7342 0.2658; ...
      0.3754 0.6246; ...
      0.5140 0.4860; ...
      0.8094 0.1906];

mu = [0.320 1.143; ...
      0.7962 2.4075; ...
      2.383 6.070; ...
      11.23 13.27; ...
      301.1 529.6; ...
      2548 6366];

sg = [0.1712 0.5622; ...
      0.393 1.406; ...
      0.841 2.289; ...
      2.427 2.238; ...
      137.0 176.3; ...
      1475 2133];
 
% load contestant predictions
[xname prm1] = textread(fullfile(path_to_pred, ['dream6_parest_parameters_model_' int2str(1) '_' team_name '.txt']), '%s %f');
[xname prm2] = textread(fullfile(path_to_pred, ['dream6_parest_parameters_model_' int2str(2) '_' team_name '.txt']), '%s %f');
[xname prm3] = textread(fullfile(path_to_pred, ['dream6_parest_parameters_model_' int2str(3) '_' team_name '.txt']), '%s %f');
    
[t p11 p12 p13] = textread(fullfile(path_to_pred, ['dream6_parest_timecourse_model_' int2str(1) '_' team_name '.txt']), '%f %f %f %f', 'headerlines',1);
[t p21 p22 p23] = textread(fullfile(path_to_pred, ['dream6_parest_timecourse_model_' int2str(2) '_' team_name '.txt']), '%f %f %f %f', 'headerlines',1);
[t p31 p32 p33] = textread(fullfile(path_to_pred, ['dream6_parest_timecourse_model_' int2str(3) '_' team_name '.txt']), '%f %f %f %f', 'headerlines',1);
    
% load gold standard
[xname prm1_] = textread(fullfile(path_to_gs, ['model' int2str(1) '_parameters_answer.txt']), '%s %f');
[xname prm2_] = textread(fullfile(path_to_gs, ['model' int2str(2) '_parameters_answer.txt']), '%s %f');
[xname prm3_] = textread(fullfile(path_to_gs, ['model' int2str(3) '_parameters_answer.txt']), '%s %f');
    
[t p11_ p12_ p13_] = textread(fullfile(path_to_gs, ['model' int2str(1) '_prediction_answer.txt']), '%f %f %f %f', 'headerlines',1);
[t p21_ p22_ p23_] = textread(fullfile(path_to_gs, ['model' int2str(2) '_prediction_answer.txt']), '%f %f %f %f', 'headerlines',1);
[t p31_ p32_ p33_] = textread(fullfile(path_to_gs, ['model' int2str(3) '_prediction_answer.txt']), '%f %f %f %f', 'headerlines',1);

% calculate distances and p-values
distances = zeros(1,6);
pvalues = zeros(1,6);

distances(1) = sum((log(prm1 ./ prm1_)).^2) / length(prm1_);
pvalues(1) = pi(1,1)*gamcdf(distances(1), (mu(1,1)/sg(1,1))^2, (sg(1,1)^2)/mu(1,1)) + pi(1,2)*gamcdf(distances(1), (mu(1,2)/sg(1,2))^2, (sg(1,2)^2)/mu(1,2));
distances(2) = sum((log(prm2 ./ prm2_)).^2) / length(prm2_);
pvalues(2) = pi(2,1)*gamcdf(distances(2), (mu(2,1)/sg(2,1))^2, (sg(2,1)^2)/mu(2,1)) + pi(2,2)*gamcdf(distances(2), (mu(2,2)/sg(2,2))^2, (sg(2,2)^2)/mu(2,2));
distances(3) = sum((log(prm3 ./ prm3_)).^2) / length(prm3_);
pvalues(3) = pi(3,1)*gamcdf(distances(3), (mu(3,1)/sg(3,1))^2, (sg(3,1)^2)/mu(3,1)) + pi(3,2)*gamcdf(distances(3), (mu(3,2)/sg(3,2))^2, (sg(3,2)^2)/mu(3,2));
    
p1 = [p11(12:end) p12(12:end) p13(12:end)]; p1_ = [p11_(12:end) p12_(12:end) p13_(12:end)];
distances(4) = sum(sum(((p1 - p1_).^2) ./ (0.01 + 0.01*p1_.^2))) / 90;
pvalues(4) = pi(4,1)*gamcdf(distances(4), (mu(4,1)/sg(4,1))^2, (sg(4,1)^2)/mu(4,1)) + pi(4,2)*gamcdf(distances(4), (mu(4,2)/sg(4,2))^2, (sg(4,2)^2)/mu(4,2));
p2 = [p21(12:end) p22(12:end) p23(12:end)]; p2_ = [p21_(12:end) p22_(12:end) p23_(12:end)];
distances(5) = sum(sum(((p2 - p2_).^2) ./ (0.01 + 0.01*p2_.^2))) / 90;
pvalues(5) = pi(5,1)*gamcdf(distances(5), (mu(5,1)/sg(5,1))^2, (sg(5,1)^2)/mu(5,1)) + pi(5,2)*gamcdf(distances(5), (mu(5,2)/sg(5,2))^2, (sg(5,2)^2)/mu(5,2));
p3 = [p31(12:end) p32(12:end) p33(12:end)]; p3_ = [p31_(12:end) p32_(12:end) p33_(12:end)];
distances(6) = sum(sum(((p3 - p3_).^2) ./ (0.01 + 0.01*p3_.^2))) / 90;
pvalues(6) = pi(6,1)*gamcdf(distances(6), (mu(6,1)/sg(6,1))^2, (sg(6,1)^2)/mu(6,1)) + pi(6,2)*gamcdf(distances(6), (mu(6,2)/sg(6,2))^2, (sg(6,2)^2)/mu(6,2));

score = -log(prod(pvalues));









  
