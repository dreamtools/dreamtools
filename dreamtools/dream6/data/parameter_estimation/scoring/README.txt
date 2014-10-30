  [distances pvalues score] = score_ch2(path_to_pred, path_to_gs, team_name)
  Scores predictions for DREAM6, Callenge 2. Outputs p-values and distances
  to the gold standard in the following order:
  1. Parameters Model 1
  2. Parameters Model 2
  3. Parameters Model 3
  4. TimeCourse Model 1
  5. TimeCourse Model 2
  6. TimeCourse Model 3
 
  Input:
  path_to_pred - path to the directory with prediction files
  path_to_gs - path to the directory with gold standard files
  team_name - the name of the team
 
  Output:
  distances - distances to gold standard
  pvalues - p-values for each individual distance
  score - final score calculated as -log(prod(pvalues))
 
  Note: Prediction files need to be in the same format as gold standard
  files. File names should follow this naming convention:
  dream6_parest_parameters_model_<i>_<team_name>.txt and
  dream6_parest_timecourse_model_<i>_<team_name>.txt