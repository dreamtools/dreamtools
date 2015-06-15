# -*- python -*-
# -*- coding: utf-8 -*-
#
#  This file is part of dreamtools software
#
#  Copyright (c) 2013-2015 - EBI-EMBL
#
#  File author(s): Thomas Cokelaer <cokelaer@ebi.ac.uk>
#
#  Distributed under the GPLv3 License.
#  See accompanying file LICENSE.txt or copy at
#      http://www.gnu.org/licenses/gpl-3.0.html
#
#  website: http://github.com/dreamtools
#
##############################################################################
"""Module to manage submissions"""
import copy
import dateutil.parser
import json
import scoring

from datetime import datetime, date
from dateutil.relativedelta import *
from dateutil import tz

import numpy as np
import pylab

from dreamtools.core.sageutils import Login

__all__  = ["SubmissionTools", "SC1ASubmissions", "SC1BSubmissions",
    "SC2BSubmissions", "SC2BSubmissions"]


class SubmissionTools(Login):
    """Utilities to manipulate list of submissions.

    .. note:: Used in hpn module and SCXYSubmissions classes but users
        do not need this module. For book keeping only.

    .. seealso:: ranking module

    This class could be used to attach information to submissions, load the
    status from synapse and attached it to the submissions, plot summary,
    and as a base class for the different sub challenges.::

        h = HPN.Admin()
        submissions = h.get_submissions_network( status="all")

        subs = hpn.SubmissionTools()
        submissions = subs.attach_status_to_submissions(submissions)
        submissions = subs.attach_week_to_submissions(submissions)

        [(sub['submitterAlias'], sub['week'], sub['createdOn'],
            sub['substatus']['status'], sub['substatus']['score']) for sub in
            submissions]

    """
    def __init__(self, client=None, username=None, password=None, name="notset"):
        super(SubmissionTools, self).__init__(client=client)
        self.sc1a_weeks = {
            1: ("2013-07-15T08:00:00.000Z", "2013-07-30T08:00:00.000Z"),
            2: ("2013-07-30T08:00:00.000Z", "2013-08-06T11:00:00.000Z"),  # was published using 11am
            3: ("2013-08-06T11:00:00.000Z", "2013-08-13T08:00:00.000Z"),
            4: ("2013-08-13T08:00:00.000Z", "2013-08-20T08:00:00.000Z"),
            5: ("2013-08-20T08:00:00.000Z", "2013-08-27T08:00:00.000Z"),
            6: ("2013-08-27T08:00:00.000Z", "2013-09-03T08:00:00.000Z"),
            7: ("2013-09-03T08:00:00.000Z", "2013-09-10T08:00:00.000Z"),
            8: ("2013-09-10T08:00:00.000Z", "2013-09-17T08:00:00.000Z"),
            9: ("2013-09-17T08:00:00.000Z", "2013-09-23T08:00:00.000Z"),
            10: ("2013-09-23T08:00:00.000Z", "2013-09-30T08:00:00.000Z"),
            "collaborative": ("2013-11-01T08:00:00.000Z", "2014-01-31T08:00:00.000Z")
        }

        self.sc1b_weeks = {
            1: ("2013-07-15T08:00:00.000Z", "2013-07-30T08:00:00.000Z"),
            2: ("2013-07-30T08:00:00.000Z", "2013-08-06T08:00:00.000Z"),
            3: ("2013-08-06T08:00:00.000Z", "2013-08-13T08:00:00.000Z"),
            4: ("2013-08-13T08:00:00.000Z", "2013-08-20T08:00:00.000Z"),
            5: ("2013-08-20T08:00:00.000Z", "2013-08-27T08:00:00.000Z"),
            6: ("2013-08-27T08:00:00.000Z", "2013-09-03T08:00:00.000Z"),
            7: ("2013-09-03T08:00:00.000Z", "2013-09-10T08:00:00.000Z"),
            8: ("2013-09-10T08:00:00.000Z", "2013-09-17T08:00:00.000Z"),
            9: ("2013-09-17T08:00:00.000Z", "2013-09-23T08:00:00.000Z"),
            10: ("2013-09-23T08:00:00.000Z", "2013-09-30T08:00:00.000Z"),
            "collaborative": ("2013-11-01T08:00:00.000Z", "2014-01-31T08:00:00.000Z")
        }

        self.sc2a_weeks = {
            1: ("2013-07-15T08:00:00.000Z", "2013-08-13T08:00:00.000Z"),
            2: ("2013-08-13T08:00:00.000Z", "2013-08-20T08:00:00.000Z"),
            3: ("2013-08-20T08:00:00.000Z", "2013-08-27T08:00:00.000Z"),
            4: ("2013-08-27T08:00:00.000Z", "2013-09-03T08:00:00.000Z"),
            5: ("2013-09-03T08:00:00.000Z", "2013-09-10T08:00:00.000Z"),
            6: ("2013-09-10T08:00:00.000Z", "2013-09-17T08:00:00.000Z"),
            7: ("2013-09-17T08:00:00.000Z", "2013-09-23T08:00:00.000Z"),
            8: ("2013-09-23T08:00:00.000Z", "2013-09-30T08:00:00.000Z"),
            "collaborative": ("2013-11-01T08:00:00.000Z", "2014-01-31T08:00:00.000Z")
        }

        self.sc2b_weeks = {
            1: ("2013-07-15T08:00:00.000Z", "2013-08-20T08:00:00.000Z"),
            2: ("2013-08-20T08:00:00.000Z", "2013-08-27T08:00:00.000Z"),
            3: ("2013-08-27T08:00:00.000Z", "2013-09-03T08:00:00.000Z"),
            4: ("2013-09-03T08:00:00.000Z", "2013-09-10T08:00:00.000Z"),
            5: ("2013-09-10T08:00:00.000Z", "2013-09-17T08:00:00.000Z"),
            6: ("2013-09-17T08:00:00.000Z", "2013-09-23T08:00:00.000Z"),
            7: ("2013-09-23T08:00:00.000Z", "2013-09-30T08:00:00.000Z"),
            "collaborative": ("2013-11-01T08:00:00.000Z", "2014-01-31T08:00:00.000Z")
        }
        self.name = name
        self.submissions = []

    def attach_week_to_submissions(self, submissions , challenge):
        for i,submission in enumerate(submissions):
            week = self.get_week_submission(submission, challenge=challenge)
            submission['week'] = week
        return submissions

    def _keep_latest_only(self):
        submitters = self.get_unique_submitters()
        latest = []
        for submitter in submitters:
            subs = [x for x in self.submissions if x['userId'] == submitter]
            latest.append(subs[-1])
        return latest

    def get_week_submission(self, submission, challenge=None):
        assert challenge in ["sc1a", "sc1b", "sc2a", "sc2b"]
        d = dateutil.parser.parse(submission['createdOn'])

        if challenge == "sc1a":
            weeks = self.sc1a_weeks
        elif challenge == "sc1b":
            weeks = self.sc1b_weeks
        elif challenge == "sc2a":
            weeks = self.sc2a_weeks
        elif challenge == "sc2b":
            weeks = self.sc2b_weeks
        else:
            raise NotImplementedError

        result = None
        for week in sorted(weeks.keys()):
            dstart = dateutil.parser.parse(weeks[week][0])
            dend = dateutil.parser.parse(weeks[week][1])
            if d >= dstart and d<=dend:
                if result !=None:
                    raise ValueError("found submission in 2 weeks ???")
                else:
                    result = week

        if result == None: # check before ?
            dstart = dateutil.parser.parse(weeks[1][0])
            if d <= dstart:
                result = 0
        return result

    def attach_status_to_submissions(self, submissions):
        for i,submission in enumerate(submissions):
            print("attaching status to sub %s" % i)
            substatus = self.client.getSubmissionStatus(submission['id'])
            submission['substatus'] = copy.deepcopy(substatus)
        return submissions

    def summary(self, show="all"):
        ranks = np.argsort([sub['ranking'] for sub in self.submissions])
        for i in ranks:
            sub = self.submissions[i]
            print("%10s | %5s |%5s |%s|  %s |%s" % (sub['userId'], sub['submitterAlias'],sub['week'],
                sub['substatus']['status'], sub['ranking'],sub['zscore']))

    def attach_user_profile(self, submissions):
        for i, submission in enumerate(submissions):
            print("fetching profile of user %s" % i)
            profile = self.client.getUserProfile(submission['userId'])
            submission['userProfile'] = profile.copy()
        return submissions

    def get_unique_submitters(self):
        return list(set([x['userId'] for x in self.submissions]))


class SC1ASubmissions(SubmissionTools):
    """Retrieve SCORED submissions and attach all relevant information

    >>> s = SC1ASubmissions(final=True)
    >>> s.load_submissions()
    >>> len(s.submissions)


    final = True means that 4 combi of cell line/ligands will be ignored. See
    code

    """
    def __init__(self, client=None, name="SC1A", final=True):
        super(SC1ASubmissions, self).__init__(client=client, name=name)
        from hpn import HPNAdmin
        self.hpn = HPNAdmin(client=self.client)
        self.final = final

    def load_submissions(self, startweek=0, endweek=9, keep_latest=True):
        """Loads all SCORED submissions from SC1A

        Attaches the week, status, ranking and zscores

        """
        # load all scored submissions
        self.submissions = self.hpn.get_submissions_network(status="SCORED")
        print("Got %s SCORED submissions" % len(self.submissions))

        # attach week and filter the submissions
        self.submissions = self.attach_week_to_submissions(self.submissions, "sc1a")
        self.submissions = [sub for sub in self.submissions if sub['week']<=endweek]
        self.submissions = [sub for sub in self.submissions if sub['week']>=startweek]
        print("Keeping %s submissions in the week range requested" % len(self.submissions))

        if keep_latest:
            self.submissions = self._keep_latest_only()
            print("Keep %s latest scored submissions " % len(self.submissions))
        #assert len(self.submissions) == 83, "There were 83 submissions valid in  SC1A"

        # attach the zscore
        print("attaching submissions")
        self.submissions = self.attach_status_to_submissions(self.submissions)

        print("remove some users")
        self.remove_users()

        print("attaching scores and compute final ranking")
        self._attach_zscores() #  attach zscores
        print("all submissions available in the **submissions** attribute")
        #return self.submissions

    def remove_users(self, userIds=["375805", "1971259", "1991105", "1961142",
    "2208193", "2154231", "2200202", "2197351", "375570"]):
        """Remove some users to get final submissions

            * 375805 alphabeta is a test from TC
            * sakevin is the same team as sakev Last submission by sakve in on week
              8. sakevin submitted last on week 2 so can be ignored (userId 1991105)
            * hd systems submitted with 2 userId:
              [(u'1967990', u'HD_Systems', u'Michael Zengerling', 8)]
              [(u'1971259', u'HD_Systems', u'Ruth Grosseholz', 7)]
              The latest has the best score (week 8) so I suspect this is the one to be
              used.
            * SHCH and tongki aliases correspond to the same userId. tongji
              submitted last

        From Steven's analysis, some results are highly correlated:

            * ams1012,cas3,cas4 are the same submission. We keep only ams1012
              cas3 1961142, cas4 2208193 should be removed.
            * gucas (2154231) is same as Zhangroup. gucas removed
            * Dream5607 (2200202) and Pitt.transmed are the same. Remove Dream5607
            * sfntt has same alias but 2 different userId. Remove 2197351 so that
              the latest remains only.
            * same with SBIT 375570


        """
        submissions = [x for x in self.submissions if x['userId'] not in userIds]
        self.submissions = submissions

    def _get_ranking(self):
        ranking = scoring.HPNScoringNetwork_ranking()
        for i,sub in enumerate(self.submissions):
            auc = json.loads(sub['substatus']['report'])
            ranking.add_auc(auc, sub['submitterAlias'] +"_"+ str(i))
        return ranking

    def _attach_zscores(self):
        """attach mean zscore, 32 individual zscores
        """
        ranking = self._get_ranking()
        zscores = ranking.get_mean_zscores()

        # need to remove the 4 cell lines that causes trouble. cannot be done in
        # ranking function

        ranks = ranking.get_mean_ranks()
        for i,participant in enumerate(ranking.participants):
            # mean zscore
            self.submissions[i]['zscore'] = zscores[participant]
            # 32 individual zscores
            self.submissions[i]['zscores'] = ranking._get_zscores(ranking.aucs[i])
            # final rank
            self.submissions[i]['ranking'] = ranks[participant]
            # 32 individual ranks
            self.submissions[i]['ranks'] =  ranking.get_rank_participant(participant)
            # 32 individual AUCS
            self.submissions[i]['aucs'] =  ranking.aucs[i]
            this = ranking.aucs[i]
            self.submissions[i]['mean_aucs'] =  np.mean([this[k1][k2] for k1 in this.keys()
                for k2 in this[k1].keys()])

    def summary_final(self, show="all"):
        print("Remove 3 combi of cell line/ligands before printing")
        ranks = np.argsort([sub['ranking'] for sub in self.submissions])
        header = ("Final Rank", "Team name", "Team Id", "Submission Id", "Entity Id", "mean AUC", "mean Rank")
        print("| %12s | %20s | %20s | %20s| %20s | %12s  | %12s | " %  header)
        print("|%s|%s|%s|%s|%s|%s|%s|" % ("-"*12, "-"*20, "-"*12, "-"*12, "-"*12,"-"*12, "-"*12))

        results = {}
        res = {}
        for count, i in enumerate(ranks):
            sub = self.submissions[i]
            pvalue = 0
            if sub['submitterAlias'] == "ChaosLab":
                sub['submitterAlias'] = "FreiburgBiossX"
            data = (count+1, sub['submitterAlias'], sub['userId'],
                sub['substatus']['id'], sub['substatus']['entityId'],
                sub['mean_aucs'],sub['ranking'], pvalue)
            print("|%12s | %20s | %12s |%12s| %12s | %10.6s |%12.6s|%s|" % data)
            res[sub['submitterAlias']] = count+1
            results[sub['submitterAlias']] = data[:]
        return results


class SC1BSubmissions(SubmissionTools):
    def __init__(self, client=None, name="SC1B"):
        super(SC1BSubmissions, self).__init__(client=client, name=name)
        from hpn import HPNAdmin
        self.hpn = HPNAdmin(client=self.client)

    def load_submissions(self, startweek=0, endweek=9, keep_latest=True):
        """Loads all SCORED submissions from SC1B

        Attaches the week, status, ranking and zscores

        """
        # load all scored submissions
        self.submissions = self.hpn.get_submissions_network_insilico(status="SCORED")
        print("Got %s SCORED submissions" % len(self.submissions))

        # attach week and filter the submissions
        self.submissions = self.attach_week_to_submissions(self.submissions, "sc1b")
        self.submissions = [sub for sub in self.submissions if sub['week']<=endweek]
        self.submissions = [sub for sub in self.submissions if sub['week']>=startweek]
        print("Keeping %s submissions in the week range requested" % len(self.submissions))

        if keep_latest:
            self.submissions = self._keep_latest_only()
            print("Keep %s latest scored submissions " % len(self.submissions))

        # attach the zscore
        print("attaching submissions")
        self.submissions = self.attach_status_to_submissions(self.submissions)

        print("remove soem users")
        self.remove_users()

        print("attaching scores and compute final ranking")
        self._attach_zscores() #  attach zscores
        print("all submissions available in the **submissions** attribute")
        #return self.submissions

    def remove_users(self, userIds=["375805", "1971259", "1961142", "2208193",
        "2154231", "2023612", "2200202"]):
        """

        * 375805 alphabeta is a test from TC
        * 1971259 HD_systems has 2 ID see SC1A remove_users function.

        # From Steven's analysis, some results are highly correlated:

        * ams1012,cas3,cas4 are the same submission. We keep only ams1012
          cas3 1961142, cas4 2208193 should be removed.
        * gucas (2154231) is same as Zhangroup. gucas removed
        * remove chilin 2023612
        * Dream5607 (2200202) and Pitt.transmed are the same. Remove Dream5607
        * sfntt has same alias but 2 different userId. Remove 2197351 so that
          the latest remains only.

        """
        submissions = [x for x in self.submissions if x['userId'] not in userIds]
        self.submissions = submissions

    def _attach_zscores(self):
        """attach mean zscore, 32 individual zscores
        """

        aucs = []
        for i, submission in enumerate(self.submissions):
            report = json.loads(submission['substatus']['report'])
            auc = report['auc']
            aucs.append(auc)
        ranks = np.argsort(aucs)[::-1] # sort a
        for i, rank in enumerate(ranks):
            self.submissions[rank]['ranking'] = i
            report = json.loads(self.submissions[i]['substatus']['report'])
            self.submissions[i]['auc'] = report['auc']
            self.submissions[i]['zscore'] = report['score']

    def summary_final(self):

        header = ("Final rank", "Team name", "userID", "synapse ID", "entityID" , "AUC", "zscore", "p-value")
        print("| %12s | %20s | %20s | %20s | %12s  | %12s | %12s | %12s |" %  header)
        print("|%s|%s|%s|%s|%s|%s|" % ("-"*12, "-"*20, "-"*12, "-"*12,"-"*12, "-"*12))
        ranks = np.argsort([sub['ranking'] for sub in self.submissions])
        results = {}
        for count, i in enumerate(ranks):
            sub = self.submissions[i]
            pvalue = 0
            if sub['submitterAlias'] == "ChaosLab":
                sub['submitterAlias'] = "FreiburgBiossX"


            data = (count+1, sub['submitterAlias'], sub['userId'],
                        sub['substatus']['id'], sub['substatus']['entityId'],
                    sub['auc'], sub['zscore'], pvalue)
            print("|%12s | %20s | %20s | %20s | %10.6s|  %10.6s |%10.6s |%12.6s|" % data)
            results[sub['submitterAlias']] = data[:]
        return results


class SC2ASubmissions(SubmissionTools):
    def __init__(self, client=None, name="SC2A"):
        super(SC2ASubmissions, self).__init__(client=client)
        # should be here to avoid import cycling
        from hpn import HPNAdmin
        self.hpn = HPNAdmin(client=self.client)

    def load_submissions(self, startweek=0, endweek=9, keep_latest=True):
        """Loads all SCORED submissions from SC2A

        Attaches the week, status, ranking and zscores

        """
        # load all scored submissions
        self.submissions = self.hpn.get_submissions_prediction(status="SCORED")
        print("Got %s SCORED submissions" % len(self.submissions))

        # attach week and filter the submissions
        self.submissions = self.attach_week_to_submissions(self.submissions,"sc2a")
        self.submissions = [sub for sub in self.submissions if sub['week']<=endweek]
        self.submissions = [sub for sub in self.submissions if sub['week']>=startweek]
        print("Keeping %s submissions in the week range requested" % len(self.submissions))

        if keep_latest:
            self.submissions = self._keep_latest_only()
            print("Keep %s latest scored submissions " % len(self.submissions))

        # attach the zscore
        print("attaching submissions")
        self.submissions = self.attach_status_to_submissions(self.submissions)

        print("remove some users")
        self.remove_users()

        print("attaching scores and compute final ranking")
        self._attach_zscores() #  attach zscores
        print("all submissions available in the **submissions** attribute")

        for sub in self.submissions:
            rmse = json.loads(sub['substatus']['report'])
            sub['old_rmses'] = copy.deepcopy(rmse)

    def remove_users(self, userIds=["375805", "1991105", "1971259"]):
        """

        * 375805 alphabeta is a test from TC
        * 1991105 sakve from week 5 has different id from sakev week 6. renmove
          week5 that has a lower score anyway
        * HD systems see SC1A function docstring 1971259

        """
        submissions = [x for x in self.submissions if x['userId'] not in userIds]
        self.submissions = submissions

    def _get_ranking(self):
        print("Getting ranking")
        import json
        ranking = scoring.HPNScoringPrediction_ranking()
        for i,sub in enumerate(self.submissions):
            rmse = json.loads(sub['substatus']['report'])
            filename = self.client.getSubmission(sub, downloadFile=True, ifcollision="keep.local")['filePath']
            print(i, filename)
            s = scoring.HPNScoringPrediction(filename)
            s.compute_all_rmse()
            rmse = copy.deepcopy(s.rmse)

            ranking.add_rmse(rmse, sub['submitterAlias'] +"_"+ str(i))
        return ranking

    def get_final_pvalue(self, submission):
        from scipy import stats
        # get all zscores
        zz = submission['zscores']
        zscores = [zz[k1][k2] for k1 in zz.keys() for k2 in zz[k1].keys()]
        dof = len(zscores) * 2
        assert dof == 56

        # zscores are one-sided (could negative) so multiply by 1
        sided = 1
        total_score = sum([-2 * np.log(stats.norm.sf(x) * sided) for x in zscores])
        # this is a fisher method to combine the 32 scores.
        # chi2 survival for dof=64 and x=100 is 0.002686
        pvalue = stats.chi2.sf(total_score, dof)
        return pvalue

    def _attach_zscores(self):
        """attach mean zscore, 32 individual zscores
        """
        ranking = self._get_ranking()
        zscores = ranking.get_mean_zscores()
        ranks = ranking.get_mean_ranks()

        for i,participant in enumerate(ranking.participants):
            # mean zscore
            self.submissions[i]['zscore'] = zscores[participant]
            # 32 individual zscores
            self.submissions[i]['zscores'] = ranking._get_zscores(ranking.rmse[i])
            # final rank
            self.submissions[i]['ranking'] = ranks[participant]
            # 32 individual ranks
            self.submissions[i]['ranks'] =  ranking.get_rank_participant(participant)
            # 32 individual RMSEs
            self.submissions[i]['rmses'] =  ranking.rmse[i].copy()
            # 32 individual RMSEs
            s = ranking.rmse[i]
            data =  [s[k1][k2] for k1 in s.keys() for k2 in s[k1].keys()]
            data = [x for x in data if np.isnan(x)==False]
            mu = np.mean(data)
            self.submissions[i]['mean_rmse'] =  mu

    def summary_final(self):
        ranks = np.argsort([sub['ranking'] for sub in self.submissions])

        header = ("| Final rank| Team name | Team Id | Synapse ID |  Entity ID | mean RMSE  | mean Rank | mean zscore |")
        print(header)
        print("|--------|--------|----------|-------|----|---------------|")
        results = {}
        for i, rank  in enumerate(ranks):
            sub = self.submissions[rank]
            print("|%s | %20s | %20s | %20s | %20s|  %10.6s  | %10.6s |%10.6s |" %
                    (i+1, sub['submitterAlias'],sub['userId'],
                        sub['substatus']['id'], sub['substatus']['entityId'],sub['mean_rmse'],sub['ranking'],sub['zscore']))
            results[sub['submitterAlias']] =  i+1
        return results


class SC2BSubmissions(SubmissionTools):
    def __init__(self, client=None):
        super(SC2BSubmissions, self).__init__(client=client, name="SC2B")
        from hpn import HPNAdmin
        self.hpn = HPNAdmin(client=self.client)

    def load_submissions(self, startweek=0, endweek=9, keep_latest=True):
        """Loads all SCORED submissions from SC2A

        Attaches the week, status, ranking and zscores

        """
        # load all scored submissions
        self.submissions = self.hpn.get_submissions_prediction_insilico(status="SCORED")
        print("Got %s SCORED submissions" % len(self.submissions))

        # attach week and filter the submissions
        self.submissions = self.attach_week_to_submissions(self.submissions,"sc2b")
        self.submissions = [sub for sub in self.submissions if sub['week']<=endweek]
        self.submissions = [sub for sub in self.submissions if sub['week']>=startweek]
        print("Keeping %s submissions in the week range requested" % len(self.submissions))

        if keep_latest:
            self.submissions = self._keep_latest_only()
            print("Keep %s latest scored submissions " % len(self.submissions))

        # attach the zscore
        print("attaching submissions")
        self.submissions = self.attach_status_to_submissions(self.submissions)

        print("remove soem users")
        self.remove_users()

        print("attaching scores and compute final ranking")
        self._attach_zscores() #  attach zscores
        print("all submissions available in the **submissions** attribute")
        for sub in self.submissions:
            rmse = json.loads(sub['substatus']['report'])
            sub['old_rmses'] = copy.deepcopy(rmse)

    #def remove_users(self, userIds=["375805", "1991105", "1971259"]):
    def remove_users(self, userIds=["375805", "1991105"]):
        """

        * 375805 alphabeta is a test from TC
        * 1991105 sakve from week 5 has different id from sakev week 6. renmove
          week5 that has a lower score anyway
        * HD systems see SC1A function docstring 1971259

        """
        submissions = [x for x in self.submissions if x['userId'] not in userIds]
        self.submissions = submissions

    def _get_ranking(self):
        import json
        ranking = scoring.HPNScoringPredictionInsilico_ranking()
        for i,sub in enumerate(self.submissions):
            rmse = json.loads(sub['substatus']['report'])
            filename = self.client.getSubmission(sub, downloadFile=True, ifcollision="keep.local")['filePath']
            s = scoring.HPNScoringPredictionInsilico(filename)
            s.compute_all_rmse()
            rmse = copy.deepcopy(s.rmse)
            ranking.add_rmse(rmse, sub['submitterAlias'] +"_"+ str(i))
        return ranking

    def _attach_zscores(self):
        """attach mean zscore, 32 individual zscores
        """
        ranking = self._get_ranking()
        zscores = ranking.get_mean_zscores()
        ranks = ranking.get_mean_ranks()

        for i,participant in enumerate(ranking.participants):
            # mean zscore
            self.submissions[i]['zscore'] = zscores[participant]
            # final rank
            self.submissions[i]['ranking'] = ranks[participant]
            rmse = ranking.rmse[i]
            self.submissions[i]['rmses'] = rmse

            all_rmse = [rmse[k1][k2] for k1 in rmse.keys() for k2 in rmse[k1].keys()]
            all_rmse = [x for x in all_rmse if np.isnan(x)==False] # exclude
            mean_rmse = np.mean(all_rmse)
            self.submissions[i]['mean_rmse'] = mean_rmse

    def summary(self, show="all"):
        ranks = np.argsort([sub['ranking'] for sub in self.submissions])
        print("| Rank | User Id | Submitted Alias | Week | created on | status |  RMSE | zscore | mean Rank |")
        for i, rank  in enumerate(ranks):
            sub = self.submissions[rank]
            print("|%s | %10s | %5s |%5s |%s|%s|  %10.6s  | %10.6s |%10.6s |" %
                    (i+1, sub['userId'], sub['submitterAlias'],sub['week'],
                sub['substatus']['status'],  sub['createdOn'],  sub['mean_rmse'],sub['ranking'],sub['zscore']))

    def summary_final(self):
        ranks = np.argsort([sub['ranking'] for sub in self.submissions])
        print("| Rank | Team name | SynapseId Id | mean RMSE | mean Rank | mean zscore |")
        print("|----|-----|-----|----|----|------|")

        results = {}
        for i, rank  in enumerate(ranks):
            sub = self.submissions[rank]
            print("|%s | %20s | %20s | %20s | %20s | %10.6s  | %10.6s |%10.6s |" %
                    (i+1, sub['submitterAlias'], sub['userId'],
                        sub['substatus']['id'], sub['substatus']['entityId'],
                        sub['mean_rmse'],sub['ranking'],sub['zscore']))
            results[sub['submitterAlias']] = i+1
        return results
