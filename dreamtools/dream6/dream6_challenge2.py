"""WARNING This is not the official scoring function used to score the challenge
but provides some tools that are kep it for book keeping


Scoring the challenge Parameter Estimation

This code is based on document provided by Gustavo/Julio/Raquel called
"Scoring the Parameter Estimation".

The challenge "Parameter Estimation" is also known as challenge2 in
Dream6 hence the name of the class D6C2 that should be used to
compute the scores.

:Quick Example:

    >>> from dream6_challenge2 import D6C2
    >>> d6c2 = D6C2(path_to_files='whatever_is_relevant', N=10000)
    >>> d6c2.compute_scores() # 10000 is the number of trial used to compute the null model
    >>> print d6c2 # we show the scores in alphabetic and numeric orders

For sanity check, or see where a team did badly in predicting the parameter, use::

    >>> d6c2.plot()

More functionalities are available for sanity check. For instance, one can
look more carefully at the scores per model::

    >>> d6c2.print_scores_per_model()

Or the null model as compared to all teams:

    >>> d6c2.plot_time_course_null_model()


"""
from os.path import join as pj
import csv
import glob
import os
import sys
import random

import numpy
from numpy import square, log10, sum, median, mean, std, cumsum
import numpy.random
import scipy.stats
import pylab
from pylab import semilogy, plot, clf, hold, ylim, legend, ylabel, xlabel, hist, vlines, annotate
from pylab import figure,linspace, normpdf, title, subplot, axis, pi


sigma_b = 0.1 #sigma_baseline
sigma_s = 0.1 # sigma_signal coefficient (need to be multiply by the signal itself)

# model 1, 2, 3 must contain these number of lines
nrows_parameters = {'model1':29,
                    'model2':35,
                    'model3':49}

symbols = ['Db','sg','^r','dc','hy','*m', 'ow','pk', 'vb', '<g','>r','Dc', 'sm',  '^y', 'dk', 'hw', '*r',  'ob', 'py']



class D6C2(object):
    """Utilities to compute the scoring of challenge 2

    The expected input is a main directory containing a sub-directory for each team.
    In the sub-directories, one can find the relevant data sets.

    The expected data structure is as follows. One parent directory (parameter
    :attr:`path_to_files`. Inside the parent directory will be a sub directory
    for each team. The name of ech child directory is the lower-case name of
    each team.
    The children directories contain the data sets as submitted by each team but
    expurged from old submission.

    For the challenge we expect the 6 following files to be found::

        dream6_parest_timecourse_model_1_<teamname>.txt
        dream6_parest_timecourse_model_2_<teamname>.txt
        dream6_parest_timecourse_model_3_<teamname>.txt
        dream6_parest_parameters_model_1_<teamname>.txt
        dream6_parest_parameters_model_2_<teamname>.txt
        dream6_parest_parameters_model_3_<teamname>.txt

    Finally, an additional child directory called **simulations** must be
    available and it should contain the simulated data sets. All results
    will be compared to the results found in this directory.

    Scores are computed according to a dream6 document provided (see module
    documentation).

    :Quick Example:

    First, create an instance of D6C2. It will read the simulated data in the
    directory simulations as well as all the team directories::

        data = D6C2(t_start=11, t_end=40, path_to_files='parest', verbose=True)

    .. note:: in the case of the time course results, we want to skip data sets that have
        a time below t=11 hence the arguments that sets t_start=11.

    The simulated data can be found in :attr:`time_course_simulations` and
    :attr:`parameters_simulations`. All team results are stored in a dictionary in
    :attr:`timecourse_predicted` and :attr:`parameters_predicted`.

    For the time course case, data are stored in a D6C2 structure that is a
    dictionary with keys as 'model1', 'model2', 'model3'::

        >>> c2 = D6C2(path_tofiles='test')
        >>> c2.time_course_simulated['model1']

    It returns 3 arrays (one for each protein column). In the parameters case,
    the predicted data is made of dictionaries of dictionaries::

        >>> c2 = D6C2(path_tofiles='test')
        >>> c2.time_course_predicted['teamname']['model1']

    So that c2.time_course_predicted['teanmame']['model'] has the same structure
    as c2.time_course_simulated['model1'].

    Note also that the team names are stored as attributes::

        >>> c2.teams

    but can also be retrieve from the dictionary keys::

        >>> c2.time_course_predicted.keys()

    :Distance between simulated and predicted values:

    Use the :meth:`D6C2.compute_time_course_distances` to get :math:`D_j^{prot}`
    for each model :math:`j`::

        >>> c2.compute_time_course_distances()

    :Distance between estimated and known parameters:

    Use the :meth:`D6C2.compute_parameters_distances` to get  :math:`D_j^{param}`
    for each model :math:`j`::

        >>> c2.compute_parameters_distances()

    Then, you can compute N null model based on the team results and compute the
    distribution of distance for that random model::

        >>> c2.plot_hist_parameters(10000)
        >>> c2.plot_time_course_parameters(10000)

    Where 10,000 is the number of null model to be generated.

    Finally, the :meth:`score` does all the work for you by computing the pvalues and
    the final score of each team.

        >>> c2.compute_scores()  # here you call the function
        >>> c2.scores    # here you look at the results in the attribute :attr:`scores`

    .. todo:: once N random data is computed, not need to recompute it.
        save the data once for all in an attribute. Right now, compute_scoring()
        and plot() recompute the data.
    """

    def __init__(self, t_start=11, t_end=40, N=1000, path_to_files='.',
                 verbose=False, null_model='teams', numerical=False, remove_outliers=False):
        """

        :param int t_start:
        :param int t_end:
        :param str path_to_filter: Directory where to find all team sub directories
        :param bool verbose:
        :param int N: number of random models used in the pvalues estimation.
        :param int outliers: if set to True, the outliers are removed(experimental)
            when created random data sets from team results



        :Attributes Read/Write:

         * :attr:`N` number of simulations for the null model
         * :attr:`null_model` if 'teams' (default) compute the null model based on the data sent
            by the teams. If 'range' uses uniformly distributed data in a range
            based on maximum values over all teams.
         * :attr:`kstol` is the tolerance of the KStest (default 15%) to catch very bad fits


        :Attributes Read only:

         * :attr:`Nt` stores the t_end - :attr:`t_start` time range.
         * :attr:`teams` returns list of teams read in the directory provided
         * :attr:`time` contains a range of time between t_start and t_end
         * :attr:`time_course_simulated` contains a D6C2 structure with time_course simulated data
         * :attr:`parameters_simulated` contains a D6C2 structure with parametesr simulated data
         * :attr:`time_course_predicted` contains a D6C2 structure with time_course predicted data
         * :attr:`parameters_predicted` contains a D6C2 structure with parametesr predicted data

        The simulated data are read at the creation of a D6C2 instance as well
        as all the data from teams.

        """
        # from the input arguments
        self.Nt = t_end - t_start + 1
        self.time = numpy.linspace(t_start, t_end, self.Nt)
        self.t_start = t_start
        self.path_to_files = path_to_files
        self.verbose = verbose
        self._N = N
        self._null_model = null_model # can be teams or range
        # other attribute to play with
        self.kstol = 0.20 # used in the fitting method to check normal distribution
        self._time_course_model = 'normal'
        self._parameters_model = 'gamma'
        self._rotation= 70 # for the plots
        self.numerical = numerical
        self.fontsize = 12
        self.scores = None
        self.remove_outliers = remove_outliers

        # Reading the time course simulated data that are expected to be
        # found in ./simulations
        print 'Reading the simulated data sets',
        try:
            self.time_course_simulated = self._read_data(path_to_files,
                    tag='dream6_parest_timecourse', team_name='simulations',
                    verbose=verbose)
            self.parameters_simulated = self._read_data(path_to_files,
                    tag='dream6_parest_parameters', team_name='simulations',
                    verbose=verbose)
        except Exception, e:
            print '...failed'
            print e
        finally:
            print '...done'

        # reading all team predictions
        self.time_course_predicted = {}
        self.parameters_predicted = {}

        self.teams = self._get_teams(path_to_files)
        print 'Found %s teams: ' % len(self.teams)

        for team in self.teams:
            print '---Reading data sets from %s\t' % team,
            try:
                self.time_course_predicted[team] = self._read_data(path_to_files, tag='dream6_parest_timecourse', team_name=team, verbose=verbose)
            except Exception, e:
                print 'Problem(s) while reading time course data from %s ' %(team)
                print e
            else:
                print '...done.'

            try:
                self.parameters_predicted[team] = self._read_data(path_to_files, tag='dream6_parest_parameters', team_name=team, verbose=verbose)
            except Exception, e:
                print 'Problem(s) while reading parameters data from %s ' %(team)
                print e


        # once th data is read, we compute some max/median data that will be
        # used later on in the null_model (range case).
        self._median_parameters = {'model1':[[]], 'model2':[[]], 'model3':[[]]}
        self._max_parameters = {'model1':[[]], 'model2':[[]], 'model3':[[]]}
        self._min_parameters = {'model1':[[]], 'model2':[[]], 'model3':[[]]}
        self._mean_parameters = {'model1':[[]], 'model2':[[]], 'model3':[[]]}
        self._sigma_parameters = {'model1':[[]], 'model2':[[]], 'model3':[[]]}
        for model in self._median_parameters.keys():
            for i in range(0, nrows_parameters[model]):
                sigma = std([self.parameters_predicted[team][model][0][i]
                             for team in self.teams])
                M = max([self.parameters_predicted[team][model][0][i]
                             for team in self.teams])
                m = min([self.parameters_predicted[team][model][0][i]
                             for team in self.teams])
                mu = mean([self.parameters_predicted[team][model][0][i]
                             for team in self.teams])
                med = numpy.median([self.parameters_predicted[team][model][0][i]
                             for team in self.teams])
                self._median_parameters[model][0].append(med)
                self._mean_parameters[model][0].append(mu)
                self._sigma_parameters[model][0].append(sigma)
                self._max_parameters[model][0].append(M)
                self._min_parameters[model][0].append(m)

        self._median_time_course = {'model1':[[],[],[]], 'model2':[[],[],[]], 'model3':[[],[],[]]}
        self._mean_time_course = {'model1':[[],[],[]], 'model2':[[],[],[]], 'model3':[[],[],[]]}
        self._sigma_time_course = {'model1':[[],[],[]], 'model2':[[],[],[]], 'model3':[[],[],[]]}
        self._min_time_course = {'model1':[[],[],[]], 'model2':[[],[],[]], 'model3':[[],[],[]]}
        self._max_time_course = {'model1':[[],[],[]], 'model2':[[],[],[]], 'model3':[[],[],[]]}
        for model in self._median_time_course.keys():
            for column in [0,1,2]:
                for i in range(0, self.Nt):
                    sigma = std([self.time_course_predicted[team][model][column][i]
                             for team in self.teams])
                    M = max([self.time_course_predicted[team][model][column][i]
                             for team in self.teams])
                    m = min([self.time_course_predicted[team][model][column][i]
                             for team in self.teams])
                    mu = mean([self.time_course_predicted[team][model][column][i]
                             for team in self.teams])
                    med = median([self.time_course_predicted[team][model][column][i]
                             for team in self.teams])

                    self._median_time_course[model][column].append(med)
                    self._mean_time_course[model][column].append(mu)
                    self._sigma_time_course[model][column].append(sigma)
                    self._max_time_course[model][column].append(M)
                    self._min_time_course[model][column].append(m)


        # used to store the random data so that it is not recomputed
        # except if N is changed (see N property)
        self.parameters_distances_random = None
        self.time_course_distances_random = None

        print "Data ready for processing."
        print "The fit model for the time course data will be: %s " % (self._time_course_model)
        print "The fit model for the parameters data will be: %s " % (self._parameters_model)
        print "You can change the parameter fit model to normal is needed\n\n"

        print "You can now call compute_scoring() to compute the scores stored in scores attribute\n"
        print "The default number of simulations is %s, which can be changed." % (self.N)



    def _getModelTC(self):
        return self._time_course_model
    def _setModelTC(self, model):
        assert model in ['normal'], "only the normal case is handle with the time course data"
        self._time_course_model = model
    time_course_model = property(_getModelTC, _setModelTC, None, doc="get/set time_course_model")

    def _getModelP(self):
        return self._parameters_model
    def _setModelP(self, model):
        assert model in ['normal', 'gamma'], "only normal and gamma model are handled"
        self._parameters_model = model
    parameters_model = property(_getModelP, _setModelP, None, doc="get/set parameters_model")

    def _getN(self):
        return self._N
    def _setN(self, N):
        assert N>100, "N too small, choose > 100"
        self._N = N
        # if N is changed, we reset of the null model data
        self.parameters_distances_random = None
        self.time_course_distances_random = None
    N = property(_getN, _setN, None, doc="number of simulation")

    def _getNullModel(self):
        return self._null_model
    def _setNullModel(self, null_model):
        assert null_model in ['teams', 'range']
        self._null_model = null_model
        # if null_model is changed, we reset of the null model data
        self.parameters_distances_random = None
        self.time_course_distances_random = None
    null_model = property(_getNullModel, _setNullModel, None, doc="null model choice")

    def _get_teams(self, path_to_files):
        """Look into a directory and get all the sub_directories (team names)

        :param path_to_files:
        :return: list of team names (except **simulations**).
        """
        directories = glob.glob(path_to_files + '/*')
        teams = []
        for directory in directories:
            if os.path.isdir(directory) == True:
                team = os.path.split(directory)[-1]
                if team != 'simulations':
                    teams.append(team)
            else:
                # skip files, we are only interested in sub directories for now
                pass
        return teams

    def _read_data(self, path_to_files=None, team_name='simulations',
                   tag='dream6_parest_timecourse', verbose=False):
        """Populate simulations or predicted data with the TimeCourse or
        Parameters data sets.

        :param path_to_files:
        :param team_name: must be a directory where canbe found either
            the simulations data or the team predictions
        :param tag: the expected prefix of the files.



        data are stored only after time > t_start

        """
        # reads the simulated data files, scanning to extract the columns of predictions for each model


        files = glob.glob(pj(path_to_files, team_name, '*'))
        if len(files) == 0:
            raise ValueError("Found 0 files. path to files (%s)or team name (%s)may be incorrect" % (path_to_files, team_name))
        else:
            if verbose==True:
                print 'Found %s files in %s' % (len(files), pj(path_to_files, team_name))

        # initiate the expected structure of the input data according to the tag.
        if tag == 'dream6_parest_timecourse':
            # timecourse format is made of 4 columns. first one is useless (time),
            # so keep the 3 columns for each model only
            simulations = {'model1':[[],[],[]], 'model2':[[],[],[]], 'model3':[[],[],[]]}
        elif tag == 'dream6_parest_parameters':
            simulations = {'model1':[[]], 'model2':[[]], 'model3':[[]]}

            # here are the expected names for the first column for each model
            type1 = ['p_degradation_rate', 'pro1_strength', 'pro2_strength', 'pro3_strength', 'pro4_strength', 'pro5_strength', 'pro6_strength']
            type2 = ['rbs1_strength', 'rbs2_strength', 'rbs3_strength', 'rbs4_strength', 'rbs5_strength', 'rbs6_strength']
            type3 = ['v1_Kd', 'v1_h', 'v2_Kd', 'v2_h', 'v3_Kd', 'v3_h', 'v4_Kd', 'v4_h', 'v5_Kd', 'v5_h', 'v6_Kd', 'v6_h', 'v7_Kd', 'v7_h', 'v8_Kd', 'v8_h']

            columns_names = {'model1':None, 'model2':None, 'model3':None}
            columns_names['model1'] = type1 +  type2 + type3
            columns_names['model2'] = type1 +  ['pro7_strength'] + type2 + ['rbs7_strength'] + type3 + ['v9_Kd','v9_h','v10_Kd','v10_h']
            columns_names['model3'] = type1 +  ['pro7_strength', 'pro8_strength', 'pro9_strength'] + type2 + ['rbs7_strength', 'rbs8_strength', 'rbs9_strength']
            columns_names['model3'] += type3 + ['v9_Kd','v9_h','v10_Kd','v10_h','v11_Kd', 'v11_h', 'v12_Kd', 'v12_h', 'v13_Kd', 'v13_h', 'v14_Kd', 'v14_h','v15_Kd', 'v15_h']
        else:
            raise ValueError("Only timecourse and parameters tag are valid right now.")

        # look at each file found in a directory
        for file in files:
            if verbose == True:
                print 'Looking at ', file
            # check if it tagged with model1, model2 or model3
            for this_model in [1, 2, 3]:
                model_tag = 'model' + str(this_model)
                filename = tag + '_model_' + str(this_model)
                if verbose == True:
                    print '    compare with filename ', filename,


                if filename in file:
                    if self.verbose == True: print ''
                    # read its CSV content using the tabulation delimiter only.
                    #data = csv.reader(open(file, 'r'), delimiter='\t')

                    #

                    # for the case of timecourse,
                    if tag == 'dream6_parest_timecourse':
                        # there are mix of tabs and spaces in some file so we read manually
                        data = open(file, 'r')
                        # we must skip the header
                        data.next()
                        # we also skip data until t_start is reached
                        for i in range(0, self.t_start):
                            data.next()
                        # and scan the data for the 3 last columns
                        try:
                            for row in data:
                                row = [x for x in row.split()] # manual split because of mix of space and tabs
                                for i in [0, 1, 2]:
                                    # 3 colums expected, skipped first one hence the +1.

                                    simulations[model_tag][i].append(row[i+1])
                        except Exception, e:
                            print e, row
                        # once the entire columns are parsed, convert to float.
                        simulations[model_tag][0] = numpy.array(simulations[model_tag][0], dtype=float)
                        simulations[model_tag][1] = numpy.array(simulations[model_tag][1], dtype=float)
                        simulations[model_tag][2] = numpy.array(simulations[model_tag][2], dtype=float)

                    # the parameter case
                    elif tag == 'dream6_parest_parameters':
                        data = csv.reader(open(file, 'r'), delimiter='\t')

                        # we will check that first column is correct otherwise we will compare apple and orange.
                        for count, row in enumerate(data):
                            # we skip data until t_start is reached
                            #if count < self.t_start:
                            #    pass
                            #else:
                            # 2 colums expected, skipped first one but check its content
                            if row[0] != columns_names[model_tag][count]:
                                raise ValueError("found invalid tag in first column: %s. Expected %s" % (row[0], columns_names[model_tag][count]))
                            simulations[model_tag][0].append(row[1])  # always 0 because we store only one column, always 1 because we store the second column
                        # once data is parsed, convert to float
                        simulations[model_tag][0] = numpy.array(simulations[model_tag][0], dtype=float)

                else:
                    if verbose == True:
                        print '----skipped'

        return simulations

    def _get_parameters_distance_team(self, team, model):
        """simple function use by compute_parameters_distance"""
        # get simulated data and team prediction for a specific model
        try:
            sim = self.parameters_simulated[model]
            pred = self.parameters_predicted[team][model]
        except:
            raise ValueError('model or team argument is wrong. Valid models are model1, model2 or model3.')

        D_param_model = self._get_parameters_distance(sim, pred, team, model)

        return D_param_model



    def _get_time_course_distance_team(self, team, model):
        """simple function used by compute_time_course_distance"""
        # get simulated data and team prediction for a specific model
        try:
            sim = self.time_course_simulated[model]
            pred = self.time_course_predicted[team][model]
        except:
            raise ValueError('model or team argument is wrong. Valid models are model1, model2 or model3.')

        D_prot_model = self._get_time_course_distance(sim, pred, team, model)

        return D_prot_model


    def _get_parameters_distance(self, sim, pred, team, model):
        """Compute the Distance for a given model and team

        Used by get_parameters_distance_random

        :param sim: simulated data for a given model
        :param pred: predicted data for a given team and model
        """
        D_param_model = sum(square(log10(pred[0]/sim[0])))
        D_param_model /= nrows_parameters[model]
        assert nrows_parameters[model] == len(pred[0]), "wronf size expected %s found %s" %(nrows_parameters[model], len(pred[0]))

        if self.verbose == True:
            print "Time Course Scoring team %s (model %s)=%s" % (team, model, D_param_model)
        return D_param_model

    def _get_time_course_distance(self, sim, pred, team , model):
        """Compute the Distance for a given model and team

        Used by get_time_course_distance_random

        :param sim: simulated data for a given model
        :param pred: predicted data for a given team and model
        """
        D_prot_model = 0
        sb2 = sigma_b * sigma_b
        ss2 = sigma_s * sigma_s
        for i in [0, 1, 2]:
            D_prot_model += sum(square( pred[i]-sim[i] ) / (sb2 +ss2*sim[i]*sim[i]))

        norm = 3. * self.Nt  # normalisation by 3 models and N data
        D_prot_model /= norm
        if self.verbose == True:
            print "Time Course Scoring team %s (model %s)=%s" % (team, model, D_prot_model)
        return D_prot_model

    def compute_parameters_distances(self):
        r"""Compute the distance for each team and each model :math:`D_j^{param}`

        .. math::

            D_j^{param} = \frac{1}{N} \sum^{N_p}_{i=1} \left[ \log {\frac{\nu_i^{pred}}{\nu_i^{real}}}\right]^2
        """
        self.parameters_distances =  {}

        for team in self.teams:
            self.parameters_distances[team] = {
                 'model1': self._get_parameters_distance_team(team, 'model1'),
                 'model2': self._get_parameters_distance_team(team, 'model2'),
                 'model3': self._get_parameters_distance_team(team, 'model3')}


    def compute_time_course_distances(self):
        r"""Computes the distance for each team and each model :math:`D_j^{prot}`


        .. math::

            D_j^{prot} = \frac{1}{90} \sum^{3}_{k=1}\sum_{i=11}^40 \frac{\left[p_k^{pred}(t_i) - p_k^{sim}(t_i)\right]^2}{0.01+0.01 \left[p_k^{sim}(t_i)\right]^2}
        """
        self.time_course_distances =  {}
        for team in self.teams:
            self.time_course_distances[team] = {
                 'model1': self._get_time_course_distance_team(team, 'model1'),
                 'model2': self._get_time_course_distance_team(team, 'model2'),
                 'model3': self._get_time_course_distance_team(team, 'model3')}

    def _compute_parameters_distances_random(self):
        """Create N random :math:`D_j^{param}` for each model j and compute their distances

            >>> data = c.get_parameters_distance_random(1000)
            >>> data['model1']

        """
        sim = self.parameters_simulated
        distances = {'model1':[], 'model2':[], 'model3':[]}
        print("\n")
        for _i in range(self.N):
            # just to print the time remaining
            if numpy.random.randint(0,10) == 1:
                print '%3s%%\r' % int(float(_i)/self.N*100),
            sys.stdout.flush()

            # the actual code here
            r = self._get_parameters_random()
            distances['model1'].append( self._get_parameters_distance(sim['model1'],
                                                    r['model1'], 'random', 'model1'))
            distances['model2'].append( self._get_parameters_distance(sim['model2'],
                                                    r['model2'], 'random', 'model2'))
            distances['model3'].append( self._get_parameters_distance(sim['model3'],
                                                    r['model3'], 'random', 'model3'))
        self.parameters_distances_random = distances

    def _compute_time_course_distances_random(self):
        """Create N random :math:`D_j^{prot}` for each model j and compute their distance


            >>> data = c.get_time_course_distance_random(1000)
            >>> data['model1']

        """
        N = self.N
        sim = self.time_course_simulated
        distances = {'model1':[], 'model2':[], 'model3':[]}

        print("\n")
        for _i in range(N):
            # just to print the time remaining
            if numpy.random.randint(0,10) == 1:
                print '%3s%%\r' % int(float(_i)/self.N*100),
            sys.stdout.flush()

            # actual code here below
            r = self._get_time_course_random()
            # get distance for each model
            distance = [self._get_time_course_distance(sim['model1'], r['model1'], 'random', 'model2'),
                self._get_time_course_distance(sim['model2'], r['model2'], 'random', 'model2'),
                self._get_time_course_distance(sim['model3'], r['model3'], 'random', 'model3')]
            distances['model1'].append(distance[0])
            distances['model2'].append(distance[1])
            distances['model3'].append(distance[2])

        self.time_course_distances_random = distances

    def _get_parameters_random(self):
        """Generates a single random prediction based on the user inputs"""
        M = len(self.teams)
        # build a random predictions
        null = {'model1': [[]], 'model2': [[]], 'model3': [[]]}

        # we fill the data for each model
        models = null.keys()
        for model in models:
            # and each row
            # we create a random vector of integers
            if self.null_model == 'teams':
                # a random vector
                rs = numpy.random.randint(0, M, nrows_parameters[model])
                for i in range(0, nrows_parameters[model]):
                    # to randomly select a team
                    rteam = self.teams[rs[i]]
                    # if we do not want to use some outliers
                    if self.remove_outliers == True:
                        if model == 'model1':
                            while rteam in ['cosbi-inference']:
                                rteam = self.teams[numpy.random.randint(0, M, 1)[0]]
                        #if model == 'model2':
                        #    while rteam in ['ipk_sys', 'thetasigmabeta', 'fudge', 'cosbi-inference']:
                        #        rteam = self.teams[randint(0, M, 1)[0]]
                        #if model == 'model3':
                        #    while rteam in ['fudge', 'thetasigmabeta', 'ipk_sys', 'bioprocess-engineering-group']:
                        #       rteam = self.teams[randint(0, M, 1)[0]]
                    # a trick to get rid of bad results from some teams
                    # and the corresponding data
                    rdata = self.parameters_predicted[rteam][model][0][i]
                    # to create a random model
                    null[model][0].append(rdata)
            elif self.null_model == 'range':
                for i in range(0, nrows_parameters[model]):
                    #M = median([self.parameters_predicted[team][model][0][i]
                    #         for team in self.teams])
                    med = self._median_parameters[model][0][i]
                    m = self._min_parameters[model][0][i]
                    M = self._max_parameters[model][0][i]
                    mu = self._mean_parameters[model][0][i]
                    sigma = self._sigma_parameters[model][0][i]

                    #rdata = uniform(0, self.parameters_simulated[model][0][i]*2)
                    mu = self.parameters_simulated[model][0][i]
                    rdata = -1
                    while rdata<0:
                        rdata = uniform(mu-sigma, mu+sigma)
                    null[model][0].append(rdata)

        #convert to numpy array to ease math ops
        for model in null.keys():
            null[model][0] = numpy.array(null[model][0], dtype=float)
        return null


    def _get_time_course_random(self):
        """Generates a single random prediction based on the user inputs"""

        M = len(self.teams)
        # build a random predictions
        null = {'model1': [[],[],[]], 'model2': [[],[],[]], 'model3': [[],[],[]]}

        # we fill the data for each model
        for model in null.keys():
            # and each colum
            for i in range(0, self.Nt):


                # and row
                if self.null_model == 'teams':
                    rs = numpy.random.randint(0, M, self.Nt)
                    rteam = self.teams[rs[i]]
                    for column in [0, 1, 2]:
                        # by getting a team randomly

                        # if we do not want to use some outliers
                        if self.remove_outliers == True:
                            #if model == 'model1':
                            #    while rteam in ['cosbi-inference', 'thetasigmabeta', 'synmikro']:
                            #        rteam = self.teams[randint(0, M, 1)[0]]
                            #if model == 'model2':
                            #    while rteam in ['bcb', 'ipk_sys', 'zi-bioss', 'fudge']:
                            #        rteam = self.teams[randint(0, M, 1)[0]]
                            if model == 'model3':
                                while rteam in ['alf']:
                                    #, 'giano6', 'bioprocess-engineering-group']:
                                    rteam = self.teams[numpy.random.randint(0, M, 1)[0]]
                        # and the corresponding data
                        rdata = self.time_course_predicted[rteam][model][column][i]
                        null[model][column].append(rdata)
                elif self.null_model == 'range':
                    for i in range(0, self.Nt):
                        #M = median([self.time_course_predicted[team][model][column][i]
                        #     for team in self.teams])
                        M = self._max_time_course[model][column][i]
                        m = self._min_time_course[model][column][i]
                        med = self._median_time_course[model][column][i]
                        mu = self._mean_time_course[model][column][i]
                        sigma = self._sigma_time_course[model][column][i]

                        mu = self.time_course_simulated[model][column][i]
                        rdata = -1
                        while rdata<=0:
                            rdata = uniform(mu-.1*sigma,mu+.1*sigma)
                        null[model][column].append(rdata)

        for model in null.keys():
            null[model][0] = numpy.array(null[model][0], dtype=float)
            null[model][1] = numpy.array(null[model][1], dtype=float)
            null[model][2] = numpy.array(null[model][2], dtype=float)
        #convert to numpy array to ease math ops
        return null

    def _get_parameters_mean_null_model(self):
        """build up N random prediction and return the mean vector """
        null = self._get_parameters_random()
        #null = self.simple_random_parameters()
        # N-1 since we already created an instance here line below
        for _i in range(self.N-1):
            this_null = self._get_parameters_random()
            #this_null = self.simple_random_parameters()
            for model in ['model1', 'model2', 'model3']:
                null[model][0] += this_null[model][0]
        # only 1 column hence the [0]
        for model in ['model1', 'model2', 'model3']:
            null[model][0] /= float(self.N)
        return null

    def _get_time_course_mean_null_model(self):
        """build up N random prediction and return the mean vector """

        null = self._get_time_course_random()
        #null = self.simple_random_time_course()
        for _i in range(self.N-1):
            this_null = self._get_time_course_random()
            #this_null = self.simple_random_time_course()
            for model in ['model1', 'model2', 'model3']:
                for c in [0, 1, 2]:
                    null[model][c] += this_null[model][c]
        for model in ['model1', 'model2', 'model3']:
            for c in [0, 1, 2]:
                null[model][c] /= float(self.N)
        return null

    def plot_parameters_mean_null_model(self, model, teams=None, log=False):
        """plot time course null model versus time for a given model

        It also plots all the time course predicted models (for each team)

        .. note:: this function should be used for sanity checks.

        .. plot::

            from dreamtools import dream6_challenge2
            d6c2 = dream6_challenge2.D6C2(path_to_files='../share/data/parest')
            d6c2.plot_parameters_mean_null_model('model1')

        """
        self.compute_parameters_distances()
        null = self._get_parameters_mean_null_model()

        clf()
        if log:
            semilogy(null[model][0], 'k-', label='Null model', linewidth=2)
            hold(True)
            semilogy(self.parameters_simulated[model][0], 'go-', label='Simulated', linewidth=2)
        else:
            plot(null[model][0], 'k-', label='Null model', linewidth=2)
            plot(self.parameters_simulated[model][0], 'go-', label='Simulated', linewidth=2)
            hold(True)




        if teams == None:
            for team in self.teams:
                data = self.parameters_predicted[team][model]
                plot(data[0], 'r--')
        else:
            data = self.parameters_predicted[teams][model]
            plot(data[0], 'r--')
        # plot dummy data to cheat on the legend and avoiding a legend for each team
        plot(0,0, 'r--', label='Individual team results')
        legend()
        title(model)
        xlabel('Parameters')
        ylabel(r'Meam null-model results')

    def plot_time_course_mean_null_model(self, model, teams=None, column=1, log=False):
        """plot time course null model versus a team for a given model and colum

        .. note:: this function is used for sanity checks.

        .. plot::

            from dreamtools import dream6_challenge2
            d6c2 = dream6_challenge2.D6C2(path_to_files='../share/data/parest')
            d6c2.plot_time_course_mean_null_model('model1')

        """
        N = self.N
        assert column in [1,2,3], "Only 3 columns in the time course (starts at zero)"
        column -= 1 # to use C/Python notation
        # self.compute_time_course_distances()
        null = self._get_time_course_mean_null_model()

        clf()
        if log:
            semilogy(null[model][column], 'k-', linewidth=3,label='Null model based on %s model' % N)
            hold(True)
            semilogy(self.time_course_simulated[model][0], 'go-', label='Simulated', linewidth=2)
        else:
            plot(null[model][column], 'k-', linewidth=3, label='Null model based on %s model' % N)
            hold(True)
            plot(self.time_course_simulated[model][0], 'go-', label='Simulated', linewidth=2)


        if teams == None:
            for team in self.teams:
                data = self.time_course_predicted[team][model]
                plot(data[column], 'r--')

        else:
            data = self.time_course_predicted[teams][model]
            plot(data[column], 'r--')
        # plot dummy data to cheat on the legend
        plot(0,0, 'r--', label='team individual results')
        legend()
        title(model + ' (column %s)' % (column+1))
        xlabel('Time indices')
        ylabel(r'Mean Null-model results')

    def _compute_null_model(self):
        if self.parameters_distances_random == None:
            self._compute_parameters_distances_random()
        if self.time_course_distances_random == None:
            self._compute_time_course_distances_random()

    def plot_hist_parameters(self,  model, teams=None, nbins=20):
        """Generates N random model and their scores and compare with teams' scores.

        The following code generates 1000 random distribution of the parameters
        distances for the model1 case and shows the teams distance as well (black
        vertical lines)

        .. plot::

            from dreamtools import dream6_challenge2
            d6c2 = dream6_challenge2.D6C2(path_to_files='../share/data/parest')
            d6c2.compute_parameters_distances()
            d6c2.compute_time_course_distances()
            d6c2.plot_hist_parameters(1000, 'model1')

        """
        self.compute_parameters_distances()
        self._compute_null_model()
        r = self.parameters_distances_random
        # and plot the histogram ditribution of one model
        clf()
        count, _bins, _patches = hist(r[model], nbins)
        hold(True)

        #For each team, we add a line for its own computed distance
        self._add_annotation(self.parameters_distances, model, norm=max(count))
        xlabel('$D_{%s}^{param}$' % model, fontsize=self.fontsize)
        ylabel('\#', fontsize=self.fontsize)
        title('Parameters null model distribution('+model+')')



    def plot_hist_time_course(self, model, teams=None, nbins=20):
        """Generates N random model and their distanace and compare with teams' scores.

        The following code generates 1000 random distribution of the parameters
        distances for the model1 case and shows the teams distance as well (black
        vertical lines)

        .. plot::

            from dreamtools import dream6_challenge2
            d6c2 = dream6_challenge2.D6C2(path_to_files='../share/data/parest')
            d6c2.compute_parameters_distances()
            d6c2.compute_time_course_distances()
            d6c2.plot_hist_time_course(1000, 'model1')

        """
        self.compute_time_course_distances()
        self._compute_null_model()
        r = self.time_course_distances_random

        # and plot its histogram ditribution
        clf()
        count, _bins, _patches = hist(r[model], nbins)
        hold(True)
        title('Time course ('+model+')')

        #For each team, we add a line for its own computed distance
        self._add_annotation(self.time_course_distances, model, norm=max(count) )
        xlabel('$D_{%s}^{prot}$' % model,fontsize=self.fontsize)
        ylabel('\#',fontsize=self.fontsize)
        title('Time course null model distribution ('+model+')')

    def _add_annotation(self, data, model, norm=1):
        for team in self.teams:
            x = data[team][model]
            y = norm
            vlines(x, 0, y, linewidth=3)
            annotate(team, xy=(x, y), xytext=(x,y),
                     xycoords='data', arrowprops=dict(arrowstyle="->"), rotation=self._rotation)

    def compute_pvalue_time_course(self):
        """Compute the pvalue using N random prediction


        """
        fitting = {'model1': None, 'model2':None , 'model3':None}
        # first, generate random data
        self._compute_null_model()
        d = self.time_course_distances_random

        for model in fitting.keys():
            # for each model, we fit a normal distribution
            params = self.fitting(d[model], model2fit=self._time_course_model)
            mu = params.rx2('estimate')[0] # extract mu from the R object
            std = params.rx2('estimate')[1] # extract std from the R object
            # and save the data in a dictionary
            fitting[model] = [mu, std]
        if self.numerical == False:
            # then, for each team, we compute the pvalue
            self.pvalue_time_course = {}
            for team in self.teams:
                self.pvalue_time_course[team] = {'model1':None, 'model2':None, 'model3':None}
                for model in fitting.keys():
                    mu = fitting[model][0] # get back the fitting parameter 1
                    std = fitting[model][1] #get back the fitting parameter 2
                    survival = scipy.stats.norm.sf(self.time_course_distances[team][model], loc=mu, scale=std)
                    pvalue = 1 - survival
                    if pvalue <= 1./self.N:
                        pvalue = 1./self.N
                    self.pvalue_time_course[team][model] = pvalue # compute the pvalue


        # numerical p-values
        elif self.numerical:
            self.pvalue_time_course = {}
            for team in self.teams:
                self.pvalue_time_course[team] = {'model1':None, 'model2':None, 'model3':None}

            for model in fitting.keys():
                count, X, _p = hist(self.time_course_distances_random[model], 1000)
                cumulative = cumsum(count) / float(sum(count))

                for team in self.teams:
                    index = numpy.where(X[1:]<self.time_course_distances[team][model])[0]
                    if len(index)==0:
                        index = 0
                        pvalue = 1./self.N
                    else:
                        index = index[-1]
                        pvalue = cumulative[index]
                    self.pvalue_time_course[team][model] = pvalue



        self._time_course_fitting = fitting


    def compute_pvalue_parameters(self):
        """Compute the pvalue using N random prediction


        """
        fitting = {'model1': None, 'model2':None , 'model3':None}

        # first, generate random data
        self._compute_null_model()
        d = self.parameters_distances_random



        for model in fitting.keys():
            # for each model, we fit a normal distribution
            params = self.fitting(d[model], model2fit=self._parameters_model)
            mu = params.rx2('estimate')[0] # extract mu from the R object
            std_ = params.rx2('estimate')[1] # extract std from the R object
            # and save the data in a dictionary
            fitting[model] = [mu, std_]

        if self.numerical == False:
            # then, for each team, we compute the pvalue
            self.pvalue_parameters = {}
            for team in self.teams:
                self.pvalue_parameters[team] = {'model1':None, 'model2':None, 'model3':None}
                for model in fitting.keys():

                    if self._parameters_model == 'normal':
                        mu = fitting[model][0] # get back the fitting parameter 1
                        std = fitting[model][1] #get back the fitting parameter 2
                        survival = scipy.stats.norm.sf(self.parameters_distances[team][model], loc=mu, scale=std)
                    elif self._parameters_model == 'gamma':
                        # for the gamma distribution, what is returned by MASS.fitdist is
                        # the shape then the rate
                        # In scipy the arguments are scipy.gamma.rvs(shape, size=N, scale=1/rate)
                        shape = fitting[model][0]
                        scale = 1./fitting[model][1]
                        survival = scipy.stats.gamma.sf(self.parameters_distances[team][model],
                                                    shape,scale=scale)
                    pvalue = 1. - survival
                    if pvalue <= 1./self.N:
                        pvalue = 1./self.N
                    self.pvalue_parameters[team][model] = pvalue
        # numerical p-values
        elif self.numerical:
            self.pvalue_parameters= {}
            for team in self.teams:
                self.pvalue_parameters[team] = {'model1':None, 'model2':None, 'model3':None}
            for model in fitting.keys():
                count, X, _p = hist(self.parameters_distances_random[model], 1000)
                cumulative = cumsum(count) / float(sum(count))

                for team in self.teams:
                    index = numpy.where(X[1:]<self.parameters_distances[team][model])[0]
                    if len(index)==0:
                        index = 0
                        pvalue = 1./self.N
                    else:
                        index = index[-1]
                        pvalue = cumulative[index]
                    self.pvalue_parameters[team][model] = pvalue

        self._parameters_fitting = fitting

    def compute_scores(self):
        r"""Compute the final scores for each team


        .. math::

            - \log10 \prod_{j=1}^3 p_j^{prot} p_j^{param}

        Given :math:`p_j^{prot}` and :math:`p_j^{param}` that are computed in
        :meth:`compute_all`.

        """
        # compute distances for al teams
        print 'Computing the parameters distances'
        self.compute_parameters_distances()
        print 'Computing the time course distances'
        self.compute_time_course_distances()

        # compute pvalues

        print 'Computing the parameters pvalues--------------',
        self.compute_pvalue_parameters()
        print 'done'
        print 'Computing the time course pvalues----------',
        self.compute_pvalue_time_course()
        print 'done'

        # compute scores now
        print 'Computing the Scores'
        self.scores = {}
        for team in self.teams:
            param = self.pvalue_parameters[team]
            prot = self.pvalue_time_course[team]
            product = 1
            for model in param.keys():
                product *= param[model] * prot[model]

            self.scores[team] = -log10(product)

    def plot_scores(self, nBestTeams=None, teamNames=None):
        """Plot the 3 scores of the first N best teams


        """
        if nBestTeams == None:
            nBestTeams = len(self.teams)
        else:
            assert nBestTeams <= len(self.teams)


        figure(1)
        clf()
        iscores = {}
        for model in ['model1','model2','model3']:
            scores_per_model = {}
            for team in self.teams:
                p_param = self.pvalue_parameters[team][model]
                p_prot = self.pvalue_time_course[team][model]
                scores_per_model[team] = -log10(p_prot * p_param)
            iscores[model] = scores_per_model

        # sorte the team versus scores
        import operator
        sorted_teams = [team[0] for team in sorted(self.scores.iteritems(), key=operator.itemgetter(1), reverse=True)]

        if teamNames == None:
            for i, team in enumerate(sorted_teams[0:nBestTeams]):
                theta = [0*pylab.pi, 120./180.*pylab.pi, 240./180.*pylab.pi,0]
                r = [iscores['model1'][team], iscores['model2'][team], iscores['model3'][team], iscores['model1'][team]]

                pylab.polar(theta, r, '%s-'%symbols[i], label=team.replace('_', '\_'))
                hold(True)
        else:
            for i, team in enumerate(teamNames):
                assert team in self.teams
                theta = [0*pylab.pi, 120./180.*pylab.pi, 240./180.*pylab.pi,0]
                r = [iscores['model1'][team], iscores['model2'][team], iscores['model3'][team], iscores['model1'][team]]

                pylab.polar(theta, r, '%s-'%symbols[i], label=team.replace('_', '\_'))
                hold(True)
        legend(ncol=2, loc='upper right', prop={'size':11})
        pylab.xticks([0,120./360*pi*2,240/360.*pi*2], ['score 1','score 2','score 3'])





    def plot(self, nbins=20, teams=None, logx=False, logy=False):
        """Plots all the Distances null model distribution for each model, for the
        parameters cand timne_course cases

        This functions plots the histogram of each distances null model together with
        the teams distancse. 6 plots are generated one for each model (3) for the
        parameters case and time course case. Distribution are fitted with
        normal or exponential distribution.

        :param bool log: switch to y-axis log scale
        :param int nbins: number of bins for the histograms
        """
        self.compute_time_course_distances()
        self.compute_parameters_distances()
        self._compute_null_model()
        r = self.time_course_distances_random

        # suppose normal distribution for the tc data
        for i, model in enumerate(['model1', 'model2', 'model3']):
            figure(i+1)
            clf()

            if not logx:
                count, _bins, _patches = hist(r[model], nbins, log=logy, normed=True)
            else:
                bins = pylab.logspace(log10(min(r[model])), log10(max(r[model])), nbins)
                count, _bins, _patches = hist(r[model], bins, log=logy, normed=True)
                pylab.xscale('log')

            hold(True)
            fit = self._time_course_fitting[model]
            #m = max(normpdf(_bins, fit[0],fit[1]))
            #y = max(count)/m * normpdf(_bins, fit[0],fit[1])
            x = linspace(min(_bins), max(_bins), 100)
            y = normpdf(x, fit[0],fit[1])

            if logy and logx:
                pylab.loglog(x, y, 'r-', linewidth=3)
                ylim([1e-6, max(count)*1.1])
            elif logy and not logx:
                semilogy(x, y, 'r-', linewidth=3)
                ylim([1e-6, max(count)*1.1])
            elif not logy and logx:
                pylab.semilogx(x, y, 'r-', linewidth=3)
            else:
                x = linspace(min(_bins), max(_bins), 100)
                y = normpdf(x, fit[0],fit[1])
                plot(x, y, 'r-', linewidth=3)
                ylim([0, max(count)*1.1])


            #For each team, we add a line for its own computed distance
            self._add_annotation(self.time_course_distances, model, norm=max(count))
            title(r'Time course: $D_j^{prot}$ Null model('+model+')')
            xlabel(r'Distance $D_j^{prot}$',fontsize=self.fontsize)


        # now the parameters
        if self.parameters_distances_random == None:
            self.get_parameters_distance_random()
        r = self.parameters_distances_random

        # suppose gamma distribution for the tc data
        for i, model in enumerate(['model1', 'model2', 'model3']):
            figure(i+4)
            clf()

            if not logx:
                count, _bins, _patches = hist(r[model], nbins, log=logy, normed=True)
            else:
                bins = pylab.logspace(log10(min(r[model])), log10(max(r[model])), nbins)
                count, _bins, _patches = hist(r[model], bins, log=logy, normed=True)
                pylab.xscale('log')
            hold(True)


            fit = self._parameters_fitting[model]

            x = linspace(min(_bins), max(_bins), 100)
            if self.parameters_model == 'gamma':
                y = scipy.stats.gamma.pdf(x, fit[0], scale=1./fit[1])
            else:
                y = normpdf(x, fit[0],fit[1])

            if logy and logx:
                pylab.loglog(x, y, 'r-', linewidth=3)
                ylim([1e-6, max(count)*1.1])
            elif logy and not logx:
                semilogy(x, y, 'r-', linewidth=3)
                ylim([1e-6, max(count)*1.1])
            elif not logy and logx:
                pylab.semilogx(x, y, 'r-', linewidth=3)
            else:
                plot(x, y, 'r-', linewidth=3)
                ylim([0, max(count)*1.1])




            #For each team, we add a line for its own computed distance
            self._add_annotation(self.parameters_distances, model, norm=max(count))
            title(r'Parameters: $D_j^{param}$ Null model('+model+')')
            xlabel(r'Distance $D_j^{param}$', fontsize=self.fontsize)



    def fitting(self, dist, model2fit='normal'):
        """

        :param dist: samples of a distribution
        """
        from rpy2.robjects.packages import importr
        from rpy2 import robjects
        from scipy.stats import kstest

        MASS = importr('MASS')
        assert model2fit in ['normal', 'gamma']
        params = MASS.fitdistr(robjects.FloatVector(dist), model2fit)

        if model2fit=='normal':
            mu = params.rx2('estimate')[0]
            std_ = params.rx2('estimate')[1]
            print 'Loglikelihood = %s' % params.rx2('loglik')
            print ' Mean = %s; STD = %s' % (mu, std_)

            ks = kstest(dist, 'norm', args=([mu, std_]))
            print 'KS test (twosided) D=%s' % ks[0]
            if ks[0] > self.kstol:
                raise ValueError("""Non-normal distribution found: KS test > %s%%.
                    Consider setting the attributs kstol to a larger value""" % self.kstol)


        elif model2fit=='gamma':
            shape = params.rx2('estimate')[0]
            rate = params.rx2('estimate')[1]
            scale = 1./params.rx2('estimate')[1]
            loc = 0
            print 'Loglikelihood = %s' % params.rx2('loglik')
            print ' shape = %s; Rate =%s, scale=%s' % (shape, rate, scale)
            # let us suppose that location is zero
            print shape, loc, scale
            ks = kstest(dist, 'gamma', args=([shape, 0, scale]))
            print 'KS test (twosided) D=%s' % ks[0]
            if ks[0] > self.kstol:
                raise ValueError("""Non-normal distribution found: KS test > %s%%.
                    Consider setting the attributs kstol to a larger value""", self.kstol)

        return params

    def print_time_course_distances(self):
        print("="*40+" "+"="*20+" "+"="*20+" "+"="*20)
        print("%40s %20s %20s %20s" % ("Team", ":math:`D_1^{prot}`", ":math:`D_2^{prot}`", ":math:`D_3^{prot}`"))
        print("="*40+" "+"="*20+" "+"="*20+" "+"="*20)

        m1 = [self.time_course_distances[team]['model1'] for team in self.teams]
        m2 = [self.time_course_distances[team]['model2'] for team in self.teams]
        m3 = [self.time_course_distances[team]['model3'] for team in self.teams]

        for i,team in enumerate(self.teams):
            print("%40s %20s %20s %20s" % (team, m1[i], m2[i], m3[i]))
        print("="*40+" "+"="*20+" "+"="*20+" "+"="*20)


    def print_parameters_distances(self):
        print("="*40+" "+"="*20+" "+"="*20+" "+"="*20)
        print("%40s %20s %20s %20s" % ("Team", ":math:`D_1^{param}`", ":math:`D_2^{param}`", ":math:`D_3^{param}`"))
        print("="*40+" "+"="*20+" "+"="*20+" "+"="*20)

        m1 = [self.parameters_distances[team]['model1'] for team in self.teams]
        m2 = [self.parameters_distances[team]['model2'] for team in self.teams]
        m3 = [self.parameters_distances[team]['model3'] for team in self.teams]

        for i,team in enumerate(self.teams):
            print("%40s %20s %20s %20s" % (team, m1[i], m2[i], m3[i]))
        print("="*40+" "+"="*20+" "+"="*20+" "+"="*20)


    def print_sorted_pvalue(self, datatype='parameters', model='model1'):
        assert datatype in ['parameters', 'time_course']

        # first, we retrieve all model1 results for each team
        data = dict([(team, models[model]) for team, models in self.pvalue_parameters.iteritems()])
        # then, we print the sorted list
        import operator
        sorted_x = sorted(data.iteritems(), key=operator.itemgetter(1))
        for x in sorted_x:
            print x[0], x[1]

    def print_scores_per_model(self):
        """

        prints:

        .. math::

            -\log {p_j^{prot} p_j^{param}}

        where j=1,2,3


        """

        scores = {}
        for model in ['model1','model2','model3']:
            scores_per_model = {}
            for team in self.teams:
                p_param = self.pvalue_parameters[team][model]
                p_prot = self.pvalue_time_course[team][model]
                scores_per_model[team] = -log10(p_prot * p_param)
            scores[model] = scores_per_model

        print(" ".join(["="*40 ,"="*30,"="*30, "="*30  ]))
        print "%40s %30s %30s %30s" % ('Team', 'Scores model1', 'Scores model2', 'Scores model3')
        print(" ".join(["="*40 ,"="*30,"="*30, "="*30  ]))

        for team in self.teams:
            print("%40s %30f %30f %30f" %(team,
                                          scores['model1'][team],
                                          scores['model2'][team],
                                          scores['model3'][team])  )
        print " ".join(["="*40, "="*30, "="*30, "="*30  ])


    def print_pvalues(self):
        pp = self.pvalue_parameters
        pt = self.pvalue_time_course
        formats = "%40s %15s %15s %15s %15s %15s %15s"
        formatf = "%40s %15f %15f %15f %15f %15f %15f"
        print formats % ("="*40, "="*15,"="*15,"="*15, "="*15,"="*15,"="*15   )
        print formats % ('Team','Model1(param)','Model2(param)','Model3(param)',
                               'Model1(prot)','Model2(prot)','Model3(prot)')
        print formats % ("="*40, "="*15,"="*15,"="*15, "="*15,"="*15,"="*15   )
        for team in self.teams:
            p = pp[team]
            t = pt[team]
            print formatf % (team,
                        p['model1'], p['model2'], p['model3'],
                        t['model1'], t['model2'], t['model3'])
        print formats % ("="*40, "="*15,"="*15,"="*15, "="*15,"="*15,"="*15   )


    def plot_distances_params_vs_distances_time(self):
        assert len(symbols) == len(self.teams)
        figure(4)
        clf()
        pylab.loglog([0.001,10],[0.001,10], '-k')
        hold(True)

        for model in [1,2,3]:
            figure(model)
            clf()
            pylab.loglog([0.001,10],[0.001,10], '-k')
            hold(True)
            for k, team in enumerate(self.teams):

                param = self.parameters_distances[team]['model' + str(model)]
                time = self.time_course_distances[team]['model' + str(model)]
                pylab.loglog(param, time, '-%s'%symbols[k], markersize=12, label=team)
                figure(4)
                if model == 1:
                    pylab.loglog(param, time, '-%s'%symbols[k], markersize=12, label=team)
                else:
                    pylab.loglog(param, time, '-%s'%symbols[k], markersize=12)
                figure(model)

            legend(loc='best', ncol=3, prop={'size':8})
            title('Distances params versus time course model%s' % model)
            xlabel('Distances $D_{%s}^{param}$ '%model, fontsize=self.fontsize)
            ylabel('Distances $D_{%s}^{prot}$ '%model, fontsize=self.fontsize)
        figure(4)
        legend(loc='best', ncol=3, prop={'size':8})
        title('Distances params versus time course (All models)' )
        xlabel('Distances $D_{1,2,3}^{param}$ ', fontsize=self.fontsize)
        ylabel('Distances $D_{1,2,3}^{prot}$ ', fontsize=self.fontsize)




    def plot_pred_vs_sim(self):

        symbols = ['D', 's', '|', '_', '^', 'd', 'h', '+', '*', ',', 'o', '.', '1', 'p',  'H',
 'v', 'x', '<', '>']
        colors = ['red', 'blue', 'green', 'yellow', 'black', 'gray', 'orange']

        figure(1, figsize=(20,10))
        clf()
        #parameter case
        for i, model in enumerate(['model1', 'model2','model3']):
            subplot(1, 3, i+1)
            for i, team in enumerate(self.teams):

                x1 = self.parameters_predicted[team][model][0]
                x2 = self.parameters_simulated[model][0]
                pylab.loglog(x1, x2, '%s'%symbols[i%len(symbols)], label=team);
                hold(True)
                title('Parameters %s' % model)
            pylab.loglog([1e-3, 1e2],[1e-3,1e2],'k-', linewidth=3);
            xlabel('Predicted')
            ylabel('Simulated')
            legend(loc='lower center',ncol=3, prop={'size':8}, columnspacing=1)


        figure(2,figsize=(25,10))
        clf()
        for i, model in enumerate(['model1', 'model2','model3']):
            for j, col in enumerate([0, 1, 2]):
                for k, team in enumerate(self.teams):
                    subplot(3, 3, i*3+j+1)

                    x1 = self.time_course_predicted[team][model][col]
                    x2 = self.time_course_simulated[model][col]

                    plot(x1, x2, '-%s'%symbols[k%len(symbols)], label=team);
                    hold(True);
                title('Time course %s col%s' %(model, col+1))

                plot([0, 1000],[0,1000],'-k', linewidth=3);
                if model=='model1':
                    if col==0:
                        axis([0,200,40,50])
                    elif col==1:
                        axis([0,800,0,80])
                    else:
                        axis([0,10,0,0.3])
                elif model == 'model2':
                    if col==0:
                        axis([0,20,5,10])
                    elif col==1:
                        axis([0,15,6,8])
                    else:
                        axis([0,20,0,20])
                elif model == 'model3':
                    if col==0:
                        axis([4,20,16,17])
                    elif col==1:
                        axis([0,4,0,3])
                    else:
                        axis([0,500,0,20])



                xlabel('Predicted')
                ylabel('Simulated')

                # just for the last one to save legend apart
                if i==2 and j==2 :
                    legend(loc=(1,1), ncol=1, prop={'size':11})





    def __str__(self):
        """Print the scores results

        First, it prints a table by sorting teams in alphabetical order
        Second, it prints a table by sorting teams according to their scores.

        If no scores has been computed, pritn an error message.
        """
        if self.scores:
            teams = self.teams
            teams.sort()
            str = "Scores for challenge 2\n"
            str += "=============================================\n"
            str += "Team                     | Score\n"
            str += "---------------------------------------------\n"
            for team in teams:
                str += "%20s \t | %s\n" % (team, self.scores[team])
            str += "---------------------------------------------\n"

            # sort by values (not by team names)
            import operator
            sorted_x = sorted(self.scores.iteritems(), key=operator.itemgetter(1))
            for x in sorted_x:
                str += "%20s \t | %s\n" % (x[0], x[1])


        else:
            str = "scores is empty, use the method compute_scores() first"
        return str

    def simple_random_parameters(self):
        #for double checking the correctness of _get_parameters_random
        team_results= self.parameters_predicted
        r = {'model1':[[]], 'model2':[[]], 'model3':[[]]}
        for model in r.keys():
            r[model][0] = numpy.array([team_results[self.get_random_team()][model][0][row]
                            for row in range(0, nrows_parameters[model])])
        return r

    def simple_random_time_course(self):
        #for double checking _get_time_course_random
        team_results= self.time_course_predicted
        r = {'model1':[[],[],[]], 'model2':[[],[],[]], 'model3':[[],[],[]]}
        for model in r.keys():
            r[model][0] = numpy.array([team_results[self.get_random_team()][model][0][row]
                            for row in range(0, self.Nt)])
            r[model][1] = numpy.array([team_results[self.get_random_team()][model][1][row]
                            for row in range(0, self.Nt)])
            r[model][2] = numpy.array([team_results[self.get_random_team()][model][2][row]
                            for row in range(0, self.Nt)])
        return r



    def get_random_team(self):
        return self.teams[random.randint(0, 19-1)]


def test(N=10000):
    c = D6C2(path_to_files='parest', verbose=False)
    c.plot_hist_time_course(N, 'model1')


def main():
    """Script to be used to compute scores in Challenge2


    """
    import sys
    if len(sys.argv) != 2:
        raise ValueError("USAGE: python dream6_challenge2.py path_to_team_directories")
    path = sys.argv[1]
    d6c2 = D6C2(path_to_files=path, N=1000)
    d6c2.compute_scores()
    print d6c2

if __name__ == "__main__":
    main()
