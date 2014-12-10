# -*- python -*-
# -*- coding: utf-8 -*-
#
#  This file is part of dreamtools software
#
#  Copyright (c) 2013-2014 - EBI-EMBL
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
"""Module to manage and test the HPN leaderboards

::

    e = hpn.HPNAdmin()
    submissions = e.get_submissions_network()


"""
import os
import time
import copy
import dateutil.parser
import json
import dateutil

from datetime import datetime
import dateutil.parser
from dateutil.relativedelta import *
from dateutil import tz


from dreamtools.core.sageutils import Login
from dreamtools.core.ziptools import ZIP
from scoring import *
from submissions import SubmissionTools

__all__  = ["HPNAdmin"]
# this is an evaluation that can be used for READ/WRITE and tests
test_evaluationID = 1963028

INITIAL_SUBMISSION_STATE = "RECEIVED"

# Those are the real evaluation ID not to be used for testing. Read only
hpn_evaluationIDs = ["1917801", "1917802", "1917803", "1917804", "1917805"]
SC1A_INDEX = 0
SC1B_INDEX = 1
SC2A_INDEX = 2
SC2B_INDEX = 3
SCVIS_INDEX = 4

experimentalDataID = "synxxxx"
insilicoDataID = "synyyyyy"


class HPN(Login, ZIP):
    """Base class for HPN scoring leaderboard classes"""
    def __init__(self, username=None, password=None, client=None):
        super(HPN, self).__init__(client=client)

        self.production = False
        self.subtools = SubmissionTools(client=self.client)

    def json(self, data):
        return json.dumps(data)


class HPNAdmin(HPN):
    """Class to manage the leaderboards

    .. warning::    FOR ADMINISTRATORS ONLY

    You can retrieve the submissions, compute the scores and update the
    leaderboards from here.

    """
    def __init__(self, challengeID=1720047, eid=None, username=None,
            password=None, ec2_key=None, ec2_secret=None, client=None):
        super(HPNAdmin, self).__init__(username=username, password=password,
                client=client)
        self.ec2_key = ec2_key
        self.ec2_secret = ec2_secret
        #self.mode = "latest_scored_or_latest_invalid"
        self.mode = "latest_scored_or_invalid_over_all_weeks"
        self.challengeID = challengeID

        if eid == None:
            print("WARNING: Use HPN DREAM evaluation identifiers  (%s)" % hpn_evaluationIDs)
            #self.evaluation = self.getEvaluation(evaluationID)
            self.evaluationId = hpn_evaluationIDs
        else:
            #self.evaluation = self.getEvaluation(eid)
            if isinstance(eid, list):
                self.evaluationId = eid
            else:
                self.evaluationId = [eid]
        self.profiles = {}

    def getZIPExperimentalData(self):
        filename = self.client.get(experimentalDataID, downloadFile=True)['path']
        z = self.loadZIPFile(filename)
        return z

    def downloadExperimentalMIDAS_main(self):
        """simple function to get the experimental data set from the web and
        extract those with the MIDAS and _main tags"""

        z = self.getZIPExperimentalData()
        for filename in [f.filename for f in z.filelist]:
            if 'MIDAS' in filename and "_main" in filename:
                z.extract(filename)

    def getZIPInSilicoData(self):
        filename = self.client.get(insilicoDataID, downloadFile=True)['path']
        z = self.loadZIPFile(filename)
        return z

    # This should be used only once
    def createEvaluation(self, title="HPN-DREAM Breast Cancer Challenge"):
        evaluation = self.client.createEvaluation(name=title, status="PLANNED", contentSource=self.challengeID)
        self.evaluation = copy.deepcopy(evaluation)
        return evaluation

    def setEvaluationStatus(self, status):
        # This should be used only once
        assert status in ["OPEN", "PLANNED","CLOSED", "COMPLETED", "RECEIVED"]
        evaluation = copy.deepcopy(self.evaluation)
        evaluation['status'] = status
        self.client.restPUT("/evaluation/%s" % evaluation['id'], self.json(evaluation))

    def get_submissions_per_evaluation(self, eid, status, limit=1000,offset=0):
        if status == "OPEN" or status=="INVALID" or status=="SCORED" or  status=="RECEIVED":
            uri = "/evaluation/%s/submission/all?status=%s&limit=%d&offset=%d" % (eid, status, limit, offset)
            return self.client.restGET(uri)
        elif status == "all":
            uri = "/evaluation/%s/submission/all?limit=%d&offset=%d" % (eid,limit, offset)
            return self.client.restGET(uri)
        else:
            raise NotImplementedError

    def tag_submission_as_invalid(self, submission, errormsg):
        eid = submission['id']
        URI = "/evaluation/submission/%s/status" % eid
        status = self.client.getSubmissionStatus(submission)
        if status['status'] in ["OPEN", "RECEIVED"]:
            print("Setting submission (%s) status to INVALID (%s)" % (eid, errormsg))
            status['status'] = "INVALID"
            status['report'] = errormsg
            if self.production:
                self.client.restPUT(URI, self.json(status))
            else:
                print("!!!! to update synapse, set production attribute to True")

    def filter_submissions_by_name(self, submissions, valid_tags=["-Network.zip"], filter=True):
        """Get all submissions that filenames matches one of the tag"""

        if isinstance(valid_tags, str):
            valid_tags = [valid_tags]


        print("Found a total of %s submissions" % submissions['totalNumberOfResults'])

        #print("Keeping only %s submissions with one of the following tags: %s" % (status, valid_tags))
        keeping = []
        # We need to check the validity of the file name. Done here. If a file
        # submitted has not the proper name, then it is ignored. We may want
        # more information about that
        for i, submission in enumerate(submissions['results']):
            handles = [x for x in json.loads(submission["entityBundleJSON"])['fileHandles']]

            if len(handles) == 0 :
                self.tag_submission_as_invalid(submission, "No files were found in the submission")
            else:
                filenames = [x['fileName'] for x in handles]
                found = [filename for tag in valid_tags for filename in filenames if tag in filename]
                if filter == True:
                    if len(found):
                        keeping.append(submission)
                    else:
                        print("submission with following filenames are Invalid: %s" % filenames)
                        print("  extra info: id={} date={}".format(submission['id'], submission['createdOn']))
                        self.tag_submission_as_invalid(submission, "Invalid filename provided %s " % filename)

                else:
                    keeping.append(submission)
        print("Keeping %s submissions" % len(keeping))
        return keeping

    def get_submissions_network(self, eid="1917801", status="all", filter=True):
        """Get only submission with Network.zip in their filenames"""
        print("Getting Network submissions (status %s)" % status)
        submissions = self.get_submissions_per_evaluation(eid, status=status)
        submissions = self.filter_submissions_by_name(submissions,
            ["-Collaborative.zip", "-Network-Code.zip", "-Network.zip", "result.zip"], filter=filter)
        return submissions

    def get_submissions_network_insilico(self, eid="1917802", status="all", filter=True):
        """Get only submission with Network-Insilico.zip in their filenames"""
        print("Getting Network Insilico submissions (status %s)" % status)
        submissions = self.get_submissions_per_evaluation(eid, status=status)
        submissions = self.filter_submissions_by_name(submissions, ["-Network-Insilico.zip", "insilico.zip"], filter=filter)
        return submissions

    def get_submissions_prediction(self, eid="1917803", status="all"):
        """Get only submission with Prediction.zip in their filenames"""
        submissions = self.get_submissions_per_evaluation(eid, status=status)
        submissions = self.filter_submissions_by_name(submissions, ["-Prediction.zip"])
        return submissions

    def get_submissions_prediction_insilico(self, eid="1917804", status="all"):
        """Get only submission with Prediction-Insilico.zip in their filenames"""
        submissions = self.get_submissions_per_evaluation(eid, status=status)
        submissions = self.filter_submissions_by_name(submissions, ["-Prediction-Insilico.zip"])
        return submissions

    def get_submissions_visualization(self, eid="1917805", status="all"):
        """Get only submission with Visualization.zip in their filenames"""
        submissions = self.get_submissions_per_evaluation(eid, status=status)
        submissions = self.filter_submissions_by_name(submissions, ["-Visualization.zip"])
        return submissions

    def summary(self):
        """Print information about submissions"""
        if isinstance(self.evaluationId, list):
            evaluationId = self.evaluationId[0]

        participants = self.client.restGET("/evaluation/%s/participant" % evaluationId)
        print("Evaluation Id=%s" % evaluationId)
        print("There are %s participants who have submitted so far." % participants['totalNumberOfResults'])

        print("------------------------------------------------ SC1A")
        N = len(self.get_submissions_network(status="OPEN"))
        print("There are %s OPEN submissions in SC1A\n." % N)
        N = len(self.get_submissions_network(status="SCORED"))
        print("There are %s SCORED submissions in SC1A.\n" % N)
        N = len(self.get_submissions_network(status="INVALID"))
        print("There are %s INVALID submissions in SC1A.\n" % N)


        print("----------------------------------------------- SC1B")
        N = len(self.get_submissions_network_insilico(status="OPEN"))
        print("There are %s OPEN submissions in SC1B.\n" % N)
        N = len(self.get_submissions_network_insilico(status="SCORED"))
        print("There are %s SCORED submissions in SC1B.\n" % N)
        N = len(self.get_submissions_network_insilico(status="INVALID"))
        print("There are %s INVALID submissions in SC1B.\n" % N)

        print("-------------------------------------------------- SC2A")
        N = len(self.get_submissions_prediction(status="OPEN"))
        print("There are %s OPEN submissions in SC2A.\n" % N)
        N = len(self.get_submissions_prediction(status="SCORED"))
        print("There are %s SCORED submissions in SC2A.\n" % N)
        N = len(self.get_submissions_prediction(status="INVALID"))
        print("There are %s INVALID submissions in SC2A.\n" % N)

        print("---------------------------------------------------- SC2B")
        N = len(self.get_submissions_prediction_insilico(status="OPEN"))
        print("There are %s OPEN submissions in SC2B.\n" % N)
        N = len(self.get_submissions_prediction_insilico(status="SCORED"))
        print("There are %s SCORED submissions in SC2B.\n" % N)
        N = len(self.get_submissions_prediction_insilico(status="INVALID"))
        print("There are %s INVALID submissions in SC2B.\n" % N)

    def update_submission_status(self, submission, scoring, production=False):
        """Update the status of a submission given Scoring instance

        :param int eid: identifier of the submission
        :param scoring: instance of HPNScoring with computed score
        """
        # Update of the submission status given score and status
        self.logger.debug("Updating submission status to {0}".format(scoring.status))
        eid = submission['id']
        submission_status = self.client.getSubmissionStatus(submission)
        submission_status['status'] = scoring.status
        if scoring.score: # otherwise we send a None
            submission_status['score'] = scoring.score
        submission_status['report'] = scoring.report

        print scoring.status, scoring.score, scoring.report
        if scoring.exception:
            assert scoring.status == "INVALID"
            print scoring.exception.value
            submission_status['report'] = scoring.exception.value
        print submission_status
        URI = "/evaluation/submission/%s/status" % eid
        if production == True:
            self.client.restPUT(URI, self.json(submission_status))

    def set_submission_status(self, submission, status="OPEN"):
        eid = submission['id']
        submission_status = self.client.getSubmissionStatus(submission)
        submission_status['status'] = "OPEN"
        URI = "/evaluation/submission/%s/status" % eid
        self.client.restPUT(URI, self.json(submission_status))

    def update_scores_prediction(self, production=False):
        """Not to be used if the notifier is on since score_submission_SC2A
        scores the submissions """
        print("Updating HPN-DREAM submissions related to sub challenge Prediction")
        print("===================================================================")
        print("Get all predictions related to SC2A")
        submissions = self.get_submissions_prediction(status="OPEN")
        submissions2 = self.get_submissions_network(status="RECEIVED")
        submissions = submissions + submissions2
        for i, submission in enumerate(submissions):
            print("\n--------- Scoring submissions %s " % (i+1))
            print("--- Submitter alias: %s" % submission['submitterAlias'])

            self.score_submission_SC2A(submission, 1 ,production=production)

    def update_scores_prediction_insilico(self, production=False):
        """Not to be used if the notifier is on since score_submission_SC2b
        scores the submissions """
        print("Updating HPN-DREAM submissions related to Challenge Prediction Insilico")
        print("=======================================================================")
        print("Get all predictions related to SC2B")
        submissions = self.get_submissions_prediction_insilico(status="OPEN")
        submissions2 = self.get_submissions_network(status="RECEIVED")
        submissions = submissions + submissions2
        for i, submission in enumerate(submissions):
            print("\n--------- Scoring submissions %s " % (i+1))
            print("--- Submitter alias: %s" % submission['submitterAlias'])
            self.score_submission_SC2B(submission, 1, production=production)

    def update_scores_network(self, production=False):
        """Not to be used if the notifier is on since score_submission_SC1A
        scores the submissions """
        print("Updating HPN-DREAM submissions related to sub challenge Network")
        print("===============================================================")
        print("Get all predictions related to Network sub challenge")

        # First, we need to retrieve all submissions and compute the AUC using
        submissions = self.get_submissions_network(status="OPEN")
        submissions2 = self.get_submissions_network(status="RECEIVED")
        submissions = submissions + submissions2

        for i, submission in enumerate(submissions):
            print("\n--------- Scoring submissions %s " % (i+1))
            print("--- Submitter alias: %s" % submission['submitterAlias'])
            self.score_submission_SC1A(submission, 1, production=production)

    def update_scores_network_insilico(self, production=False):
        """Not to be used if the notifier is on since score_submission_SC1B
        scores the submissions """
        print("Updating HPN-DREAM submissions related to sub challenge Network Insilico")
        print("===========================================================================")
        print("Get all predictions related to SC1B")

        # First, we need to retrieve all submissions and compute the AUC using
        # compute_score() method for the entries that are OPEN.
        submissions = self.get_submissions_network_insilico(status="OPEN")
        submissions2 = self.get_submissions_network(status="RECEIVED")
        submissions = submissions + submissions2

        for i, submission in enumerate(submissions):
            print("\n--------- Scoring submissions %s from %s " % (i+1, submission['submitterAlias']))
            self.score_submission_SC1B(submission, 1, production=production)

    def _get_ranking_network(self, submissions):
        print "Using %s submissions to compute the ranking" % len(submissions)
        ranking = HPNScoringNetwork_ranking(client=self.client)
        for i, submission in enumerate(submissions):
            try:
                print("Retrieving status %s " % i)
                teamName = submission['submitterAlias'] + "_id%s"  % i
                status = self.client.getSubmissionStatus(submission)
            except:
                print("could not retrieve teamName or status of submission %s" % submission["entityId"])
                continue
            # otherwise, let us add the auc to the ranking
            try:
                auc = json.loads(status['report'])
                if status['status'] == "SCORED":
                    ranking.add_auc(auc, teamName)
                else:
                    ranking.add_auc(None, teamName)
                # Now, let us keep track of this team name and submission index
                # for updates
            except:
                if status['status'] != "INVALID":
                    print("warning:: could not load report of submission %s-%s"
                        % (submission["entityId"], submission['submitterAlias']))
                ranking.add_auc(None, teamName)
        return ranking

    def _get_ranking_prediction(self, submissions):
        print "Using %s submissions to compute the ranking" % len(submissions)
        ranking = HPNScoringPrediction_ranking(client=self.client)
        for i, submission in enumerate(submissions):
            try:
                teamName = submission['submitterAlias'] + "_id%s"  % i
                status = self.client.getSubmissionStatus(submission)
            except:
                print("could not retrieve teamName or status of submission %s" % submission["entityId"])
                continue
            # otherwise, let us add the auc to the ranking
            try:
                rmse = json.loads(status['report'])
                if status['status'] == "SCORED":
                    ranking.add_rmse(rmse, teamName)
                else:
                    ranking.add_rmse(None, teamName)
                # Now, let us keep track of this team name and submission index
                # for updates
            except:
                print("warning:: could not load report of submission %s-%s"
                    % (submission["entityId"], submission['submitterAlias']))
                ranking.add_rmse(None, teamName)
        return ranking

    def _get_ranking_prediction_insilico(self, submissions):
        print "Using %s submissions to compute the ranking" % len(submissions)
        ranking = HPNScoringPredictionInsilico_ranking(client=self.client)
        for i, submission in enumerate(submissions):
            try:
                teamName = submission['submitterAlias'] + "_id%s"  % i
                status = self.client.getSubmissionStatus(submission)
            except:
                print("could not retrieve teamName or status of submission %s" % submission["entityId"])
                continue
            # otherwise, let us add the auc to the ranking
            try:
                rmse = json.loads(status['report'])
                if status['status'] == "SCORED":
                    ranking.add_rmse(rmse, teamName)
                else:
                    ranking.add_rmse(None, teamName)
            except:
                print("warning:: could not load report of submission %s-%s"
                    % (submission["entityId"], submission['submitterAlias']))
                ranking.add_rmse(None, teamName)
        return ranking

    def _select_submissions(self, submissions):
        submissions = self._clean_multiple_accounts(submissions)
        if self.mode == "latest_scored_or_latest_invalid":
            submissions = self._select_submissions_mode1(submissions)
        elif self.mode == "latest_scored_or_invalid_over_all_weeks":
            submissions = self._select_submissions_mode2(submissions)
        return submissions

    def _select_submissions_mode2(self, submissions):
        # Each week select the latest valid score or invalid submission
        # ignore week 0
        leaderboard = []
        weeks = list(set([s['week'] for s in submissions]))
        if 0 in weeks:
            weeks.remove(0)
        for week in weeks:
            week_submissions = [s for s in submissions if s['week'] == week]
            week_submissions = self._select_submissions_mode1(week_submissions)
            leaderboard.extend(week_submissions)
        return leaderboard

    def _clean_multiple_accounts(self, submissions):
        # known users who have different accounts:
        for sub in submissions:
            if sub['userId'] == '422256':
                sub['userId'] = '1991105'
        return submissions

    def _select_submissions_mode1(self, submissions):
        """keeps only latest scored, latest invalid and open submissions


        ignores "OPEN" and put a warning

        """

        leaderboard = []
        userIds = self._get_participants(submissions)

        # duplicated user id sakev team uses (u'422256' and '1991105')

        print("Select submissions (latest invalid or latest scored) amongst %s"% len(submissions))
        # search maximum version submitted
        for user in set(userIds):
            # need to map the indices of all entries to this user
            scored = [x for x in submissions if x['userId'] == user and x['substatus']['status'] == "SCORED"]
            unscored = [x for x in submissions if x['userId'] == user and x['substatus']['status'] in ["INVALID"]]
            stillopen = [x for x in submissions if x['userId'] == user and x['substatus']['status'] in ["RECEIVED", "OPEN"]]
            if len(stillopen):
                print("WARNING: skipping %s OPEN submissions from user %s " % (len(stillopen), user))
            # latest scored
            latest_scored = [x for x in scored if x['versionNumber'] == max([x['versionNumber'] for x in scored])]
            # latest
            latest_unscored = [x for x in unscored if x['versionNumber'] == max([x['versionNumber'] for x in unscored])]

            # in principle there sould be unique version bu it may happen that
            # someone submit a file (e.g., v1), submit it then delete, add back
            # and submit. The latest has version 1 again also it's 2 different
            # files sugmitted from the same project. In this case, we want the
            # most recent one.
            if len(latest_scored) >= 1:
                leaderboard.append(latest_scored[-1])
            if len(latest_unscored) >= 1:
                leaderboard.append(latest_unscored[-1])
        return leaderboard

    def _get_truncated_report(self, report):
        if len(report)>70:
            report = report[0:70] + "...(truncated)"
        return report

    def _get_table_participants_prediction_insilico(self, submissions,
            startweek=0, endweek=1e6):
        # we can alter these submissions because they should not be used for
        # updating synapse anymore. So we add status together with the
        # submission:
        from numpy import isnan, mean
        submissions = self.subtools.attach_status_to_submissions(submissions)
        submissions = self.subtools.attach_week_to_submissions(submissions, "sc2b")
        submissions = [sub for sub in submissions if sub['week']>startweek and sub['week']<=endweek]

        # We filter the submissions to keep only relevant submissions such as
        # the latest scored or lateste invalid defined by the mode attribute
        submissions = self._select_submissions(submissions)

        ranking = self._get_ranking_prediction_insilico(submissions)
        participants = ranking.participants[:]
        mean_ranks = ranking.get_mean_ranks()
        integer_ranks = ranking.get_integer_ranks()
        zscores = ranking.get_mean_zscores()

        lbText = ""
        from numpy import argsort
        unordered_ranks = [mean_ranks[x] for x in participants]
        indices_ordered_ranks = argsort(unordered_ranks)

        rankCounter = 0
        previousAUC = None
        for index in indices_ordered_ranks:

            this_participant = participants[index]
            submission = submissions[index]

            mean_rank = mean_ranks[this_participant]
            integer_rank = integer_ranks[this_participant]
            zscore = zscores[this_participant]

            rmse = ranking.rmse[index]
            all_rmse = [rmse[k1][k2] for k1 in rmse.keys() for k2 in rmse[k1].keys()]
            all_rmse = [x for x in all_rmse if isnan(x)==False] # exclude nan
            mean_rmse = mean(all_rmse)

            currentAUC = mean_rank
            if currentAUC != previousAUC:
                rankCounter += 1
            previousAUC = currentAUC

            # If there are N files submitted, they all have the same score, so
            # the first one can be taken only
            row = copy.deepcopy(submission)
            userId = submission['userId']
            row['rank'] = rankCounter
            row['meanrank'] = mean_rank

            # We need more information:
            if userId in self.profiles:
                profile = self.profiles[userId]
            else:
                profile = self.client.getUserProfile(userId)
                self.profiles[userId] = copy.deepcopy(profile)

            row['user'] = profile['displayName']
            substatus = submission['substatus']
            row['createdOn'] = submission['createdOn']

            row['score'] = mean_rmse
            row['status'] = substatus['status']
            row['zscore'] = zscore
            row['week'] = submission['week']
            if substatus['status'] == "INVALID":
                if "report" in substatus.keys():
                    row['score'] = self._get_truncated_report(substatus['report'])
                else:
                    row['score'] = "unknown error"


            rowText = "|%(rank)s|%(submitterAlias)s|%(name)s(v%(versionNumber)s)|%(week)s|%(entityId)s|%(score)s|%(zscore)s|%(status)s|%(meanrank)s|" % row
            lbText += "\n" + rowText
        return lbText

    def _get_table_participants_prediction(self, submissions, startweek=0,
            endweek=1e6):
        # we can alter these submissions because they should not be used for
        # updating synapse anymore. So we add status together with the
        # submission:
        from numpy import isnan, mean
        submissions = self.subtools.attach_status_to_submissions(submissions)
        submissions = self.subtools.attach_week_to_submissions(submissions, "sc2a")
        submissions = [sub for sub in submissions if sub['week']>startweek and sub['week']<=endweek]

        # We filter the submissions to keep only relevant submissions such as
        # the latest scored or lateste invalid defined by the mode attribute
        submissions = self._select_submissions(submissions)

        ranking = self._get_ranking_prediction(submissions)
        participants = ranking.participants[:]
        mean_ranks = ranking.get_mean_ranks()
        integer_ranks = ranking.get_integer_ranks()
        zscores = ranking.get_mean_zscores()

        lbText = ""
        from numpy import argsort
        unordered_ranks = [mean_ranks[x] for x in participants]
        indices_ordered_ranks = argsort(unordered_ranks)

        rankCounter = 0
        previousAUC = None
        for index in indices_ordered_ranks:

            this_participant = participants[index]
            submission = submissions[index]

            mean_rank = mean_ranks[this_participant]
            integer_rank = integer_ranks[this_participant]
            zscore = zscores[this_participant]

            rmse = ranking.rmse[index]
            all_rmse = [rmse[k1][k2] for k1 in rmse.keys() for k2 in rmse[k1].keys()]
            all_rmse = [x for x in all_rmse if isnan(x)==False] # exclude nan
            mean_rmse = mean(all_rmse)

            currentAUC = mean_rank
            if currentAUC != previousAUC:
                rankCounter += 1
            previousAUC = currentAUC

            # If there are N files submitted, they all have the same score, so
            # the first one can be taken only
            row = copy.deepcopy(submission)
            userId = submission['userId']
            row['rank'] = rankCounter
            row['meanrank'] = mean_rank

            # We need more information:
            if userId in self.profiles:
                profile = self.profiles[userId]
            else:
                profile = self.client.getUserProfile(userId)
                self.profiles[userId] = copy.deepcopy(profile)

            row['user'] = profile['displayName']
            substatus = submission['substatus']
            row['createdOn'] = submission['createdOn']

            row['score'] = mean_rmse
            row['status'] = substatus['status']
            row['zscore'] = zscore
            row['week'] = submission['week']
            if substatus['status'] == "INVALID":
                if "report" in substatus.keys():
                    row['score'] = self._get_truncated_report(substatus['report'])
                else:
                    row['score'] = "unknown error"


            rowText = "|%(rank)s|%(submitterAlias)s|%(name)s(v%(versionNumber)s)|%(week)s|%(entityId)s|%(score)s|%(zscore)s|%(status)s|%(meanrank)s|" % row
            lbText += "\n" + rowText
        return lbText

    def _get_table_participants_network(self, submissions, startweek=0,
            endweek=1e6):
        # we can alter these submissions because they should not be used for
        # updating synapse anymore. So we add status together with the
        # submission:
        submissions = self.subtools.attach_week_to_submissions(submissions, "sc1a")
        submissions = [sub for sub in submissions if sub['week']>startweek and sub['week']<=endweek]
        submissions = self.subtools.attach_status_to_submissions(submissions)

        # We filter the submissions to keep only relevant submissions such as
        # the latest scored or lateste invalid defined by the mode attribute
        submissions = self._select_submissions(submissions)

        # this is the instance to get all ranking information
        ranking = self._get_ranking_network(submissions)

        participants = ranking.participants[:]
        mean_ranks = ranking.get_mean_ranks()
        integer_ranks = ranking.get_integer_ranks()
        zscores = ranking.get_mean_zscores()

        lbText = ""
        from numpy import argsort
        unordered_ranks = [mean_ranks[x] for x in participants]
        indices_ordered_ranks = argsort(unordered_ranks)

        rankCounter = 0
        previousAUC = None
        for index in indices_ordered_ranks:

            this_participant = participants[index]
            submission = submissions[index]

            mean_rank = mean_ranks[this_participant]
            integer_rank = integer_ranks[this_participant]
            zscore = zscores[this_participant]

            currentAUC = mean_rank
            if currentAUC != previousAUC:
                rankCounter += 1
            previousAUC = currentAUC

            # If there are N files submitted, they all have the same score, so
            # the first one can be taken only
            row = copy.deepcopy(submission)
            userId = submission['userId']
            row['rank'] = rankCounter
            row['meanrank'] = mean_rank

            # We need more information:
            if userId in self.profiles:
                profile = self.profiles[userId]
            else:
                profile = self.client.getUserProfile(userId)
                self.profiles[userId] = copy.deepcopy(profile)

            row['user'] = profile['displayName']
            substatus = submission['substatus']
            row['createdOn'] = submission['createdOn']

            row['score'] = substatus['score']
            row['status'] = substatus['status']
            row['zscore'] = zscore
            row['week'] = submission['week']
            if substatus['status'] == "INVALID":
                if "report" in substatus.keys():
                    row['score'] = self._get_truncated_report(substatus['report'])
                else:
                    row['score'] = "unknown error"

            rowText = "|%(rank)s|%(submitterAlias)s|%(name)s(v%(versionNumber)s)|%(week)s|%(entityId)s|%(score)s|%(zscore)s|%(status)s|%(meanrank)s|" % row
            lbText += "\n" + rowText
        return lbText

    def _get_table_participants_network_insilico(self, submissions, startweek=0,
            endweek=1e6):
        submissions = self.subtools.attach_status_to_submissions(submissions)
        submissions = self.subtools.attach_week_to_submissions(submissions, "sc1b")
        submissions = [sub for sub in submissions if sub['week']>startweek and sub['week']<=endweek]

        # We filter the submissions to keep only INVALID and SCORED submissions
        submissions = self._select_submissions(submissions)

        # need to compute the ranking first...
        aucs = []
        for i, submission in enumerate(submissions):
            try:
                report = json.loads(submission['substatus']['report'])
                score = report['auc']
                # scores(AUC) and zscores are directly proportional except that
                # scores are between 0 and 1 and 1 means perfect and zscores are
                # between 0 and infintie and infinite is perfect. Let us work with
                # AUCS
                aucs.append(score)
            except:
                aucs.append(-1000) # should be enough. A bad score is around zero
        from numpy import argsort
        ranks = argsort(aucs)[::-1] # sort and reverse from best to worst
        lbText = ""

        #should fill the rows in the rank order

        rankCounter = 0
        previousAUC = None

        for rank_index in ranks:
            currentAUC = aucs[rank_index]
            if currentAUC != previousAUC:
                rankCounter += 1
            previousAUC = currentAUC
            submission = submissions[rank_index]
            try:
                report = json.loads(submission['substatus']['report'])
                zscore = report['score']
                auc = report['auc']
            except:
                zscore = "undefined"

            # If there are N files submitted, they all have the same score, so
            # the first one can be taken only
            row = copy.deepcopy(submission)
            userId = submission['userId']

            # We need more information:
            if userId in self.profiles:
                profile = self.profiles[userId]
            else:
                profile = self.client.getUserProfile(userId)
                self.profiles[userId] = copy.deepcopy(profile)

            row['user'] = profile['displayName']
            substatus = submission['substatus']

            row['score'] = auc
            row['zscore'] = zscore
            row['status'] = substatus['status']
            row['rank'] = rankCounter
            row['week'] = submission['week']
            if substatus['status'] == "INVALID":
                if "report" in substatus.keys():
                    row['score'] = self._get_truncated_report(substatus['report'])
                else:
                    row['score'] = "unknown error"

            rowText = "|%(rank)s|%(submitterAlias)s|%(name)s(v%(versionNumber)s)|%(week)s|%(entityId)s|%(score)s|%(status)s|%(zscore)s|" % row

            lbText += "\n" + rowText
        return lbText

    def _update_wiki_leaderboard(self, wikiId, lbText):
        raise ValueError("update the leaderboard manually please.")
        owner = self.client.get(self.challengeID)
        lbWikiPage = self.client.getWiki(owner, wikiId)
        lbWikiPage['markdown'] = lbText
        lbWikiPage = self.client.store(lbWikiPage)

    def _get_participants(self, submissions):
        participants = list(set([s['userId'] for s in submissions]))
        return participants

    def _get_week(self, challenge):
        subs = SubmissionTools(client=self.client)
        now = datetime.now(tz.tzlocal())
        for i in range(1,100000):
            if i not in subs.sc1a_weeks.keys():
                break
            if challenge == "sc1a":
                thisdate = dateutil.parser.parse(subs.sc1a_weeks[i][1])
            elif challenge == "sc1b":
                thisdate = dateutil.parser.parse(subs.sc1b_weeks[i][1])
            elif challenge == "sc2a":
                thisdate = dateutil.parser.parse(subs.sc2a_weeks[i][1])
            elif challenge == "sc2b":
                thisdate = dateutil.parser.parse(subs.sc2b_weeks[i][1])
            else:
                raise NotImplementedError
            print now, thisdate, thisdate<now
            if (thisdate < now) == False:
                return i-1


    def update_leaderboard_network(self, eid="1917801", wikiId=56830,
            production=False, filter=False):
        """ eid the Evaluation queue from which to draw submissions
            wikiId  --  the ID of the wiki to update
            production -- if True then update the wiki leaderboard, otherwise skip this step
            filter -- if True then filter out submission having illegal file names
        """
        submissions = self.get_submissions_network(eid=eid, filter=False)
        print("updating leaderboard (Network)")
        lbText = """#HPN-DREAM8 Network Inference leaderboard\n\nThis is the leaderboard of the [HPN-DREAM8 sub challenge1A](#!Wiki:syn1720047/ENTITY/56213). \n\nLast update: """ +  time.asctime()
        lbText += "\n\n|Rank|Participant|Submission Name (version)|Week|Submission id|Mean AUC|zscore|Status|mean rank|"

        lbText += self._get_table_participants_network(submissions,
                endweek=self._get_week("sc1a"))
        print(lbText)

    def update_leaderboard_network_insilico(self, eid="1917802", wikiId=56850,
            production=False, filter=False):
        submissions = self.get_submissions_network_insilico(eid=eid, filter=False)
        print("updating leaderboard (SC1B)")
        lbText = """#HPN-DREAM8 Network Inference leaderboard\n\nThis is the leaderboard of the [HPN-DREAM8 sub challenge1B](#!Wiki:syn1720047/ENTITY/56213). \n\nLast update: """ +  time.asctime()
        lbText += "\n\n|Rank|Participant|Submission Name (version)|Week|Submission id|AUC|Status|z-score|"
        lbText += self._get_table_participants_network_insilico(submissions,
                endweek=self._get_week("sc1b"))
        print(lbText)

    def update_leaderboard_prediction(self, eid="1917803", wikiId=56831,
            production=False):
        submissions = self.get_submissions_prediction(eid=eid)
        #submissions = self.get_submissions_prediction()
        print("updating leaderboard (SC2A)")
        lbText = """#HPN-DREAM8 Network Inference leaderboard\n\nThis is the leaderboard of the [HPN-DREAM8 sub challenge2A](#!Wiki:syn1720047/ENTITY/56216). \n\nLast update.""" +  time.asctime()
        lbText += "\n\n|Rank|Participant|Submission Name (version)|Week|Submission id|Mean RMSE|zscore(negative is good)|Status|score (mean rank)|"
        lbText += self._get_table_participants_prediction(submissions,
                endweek=self._get_week("sc2a"))
        print(lbText)

    def update_leaderboard_prediction_insilico(self, eid="1917804",
            wikiId=56851, production=False):
        submissions = self.get_submissions_prediction_insilico(eid=eid)
        print("updating leaderboard (SC2B)")
        lbText = """#HPN-DREAM8 Network Inference leaderboard\n\nThis is the leaderboard of the [HPN-DREAM8 sub challenge2A](#!Wiki:syn1720047/ENTITY/56216). \n\nLast update.""" +  time.asctime()
        lbText += "\n\n|Rank|Participant|Submission Name (version)|Week|Submission id|Mean RMSE|zscore(negative is good)|Status|score (mean rank)|"
        lbText += self._get_table_participants_prediction_insilico(submissions,
                endweek=self._get_week("sc2b"))
        print(lbText)

    def update_leaderboard_visualization(self):
        raise NotImplementedError

    def invalid_score(self, report):
        """ Generates an HPNScoring object for an invalid score
        """
        scoring = HPNScoring()
        scoring.status = "INVALID"
        scoring.report = report
        scoring.score = 0
        return(scoring)

    def score_submission_SC1A(self, submission, round_number, production=True):
        """ Scores the given submission and returns its status
        """
        # Get the data corresponding to this submission and compute score
        try:
            filename = self.client.getSubmission(submission, downloadFile=True)['filePath']
        except:
            filename = "dummy"
            self.logger.debug("1st try block")
            scoring = self.invalid_score("Failed to retrieve submitted file.")

        print filename
        try:
            print("scoring"),
            scoring = HPNScoringNetwork(filename=filename, verbose=False,
                client=self.client)
            if scoring.exception:
                raise scoring.exception
            scoring.compute_score()
            if scoring.exception:
                raise ScoringError
        except ScoringError:
            print("caught scoring error. will be reported")
        except Exception, e:
            self.logger.debug("2nd try blocl")
            report = "Error when scoring submission %s (version %s)" % (submission['id'], submission['versionNumber'])
            print(report)
            report += "\nError may be related to : " + type(e).__name__ +  str(e.args)
            scoring = self.invalid_score(report)

        self.update_submission_status(submission, scoring, production=production)
        self.logger.debug("Exit with status {0}".format(scoring.status))
        return (scoring)

    def score_submission_SC1B(self, submission, round_number, production=True):
        """ Scores the given submission and returns its status
        """
        # Get the data corresponding to this submission and compute score
        try:
            filename = self.client.getSubmission(submission, downloadFile=True)['filePath']
        except:
            filename = "dummy"
            self.logger.debug("1st try block")
            scoring = self.invalid_score("Failed to retrieve submitted file.")

        try:
            scoring = HPNScoringNetworkInsilico(filename=filename,
                verbose=False, client=self.client)
            if scoring.exception:
                raise scoring.exception
            score = scoring.compute_score()
            if scoring.exception:
                raise scoring.exception
            auc = scoring.get_roc().compute_auc()
            if scoring.status != None:
                raise ScoringError
        except ScoringError:
            print("caught scoring error. will be reported")
        except Exception,e:
            self.logger.debug("2nd try block")
            report = "Error when scoring submission %s (version %s)" % (submission['id'], submission['versionNumber'])
            print(report)
            report += "\nError may be related to : " + type(e).__name__ +  str(e.args)
            scoring = self.invalid_score(report)

        if scoring.status == None:
            scoring.status = "SCORED"
            scoring.score = auc
            scoring.report = json.dumps({'auc': auc, 'score':score})
        else:
            if scoring.status != None:
                scoring = self.invalid_score("""Failed to compute score in SC1B (unknown
                    error). Please contact the organisers provided the submission Id""")

        self.update_submission_status(submission, scoring, production=production)
        self.logger.debug("Exit with status {0}".format(scoring.status))
        return (scoring)

    def score_submission_SC2A(self, submission, round_number, production=True):
        """ Scores the given submission and returns its status
        """
        # Get the data corresponding to this submission and compute score
        try:
            filename = self.client.getSubmission(submission, downloadFile=True)['filePath']
        except:
            filename = "dummy"
            self.logger.debug("1st try blocl=k")
            scoring = self.invalid_score("Failed to retrieve submitted file.")

        try:
            scoring = HPNScoringPrediction(filename=filename, client=self.client)
            if scoring.exception:
                raise scoring.exception
            scoring.compute_all_rmse()
            if scoring.exception:
                raise scoring.exception
        except ScoringError:
            print("caught scoring error. will be reported")
        except Exception, e:
            self.logger.debug("2nd try block")
            report = "Unknown error when scoring submission %s (version %s)" % (submission['id'], submission['versionNumber'])
            report += "\nError may be related to : " + type(e).__name__ +  str(e.args)
            print(report)
            scoring = self.invalid_score(report)

        if scoring.status == None and len(scoring.rmse['BT20']):
            scoring.report = json.dumps(scoring.rmse)
            scoring.status = "SCORED"
            scoring.score = 1
        else:
            if scoring.status == None:
                scoring = self.invalid_score("""Failed to compute score in SC2A (unknown
                    error). Please contact the organisers provided the submission Id""")

        self.update_submission_status(submission, scoring, production=production)
        self.logger.debug("Exit with status {0}".format(scoring.status))
        return (scoring)

    def score_submission_SC2B(self, submission, round_number, production=True):
        """ Scores the given submission and returns its status
        """
        # Get the data corresponding to this submission and compute score
        try:
            filename = self.client.getSubmission(submission, downloadFile=True)['filePath']
        except:
            filename = "dummy"
            self.logger.debug("1st try block")
            scoring = self.invalid_score("Failed to retrieve submitted file.")

        print filename
        try:
            scoring = HPNScoringPredictionInsilico(filename=filename,
                client=self.client)
            if scoring.exception:
                raise scoring.exception
            scoring.compute_all_rmse()
            if scoring.exception:
                raise scoring.exception
        except ScoringError:
            print("caught scoring error. will be reported")
        except Exception, e:
            self.logger.debug("2nd try block")
            report = "Error when scoring submission %s (version %s)" % (submission['id'], submission['versionNumber'])
            report += "\nError may be related to : " + type(e).__name__ +  str(e.args)
            print(report)
            scoring = self.invalid_score(report)

        if scoring.status == None and len(scoring.rmse['AB1']):
            scoring.report = json.dumps(scoring.rmse)
            scoring.status = "SCORED"
            scoring.score = 1
        else: # is this possible that status !None
            if scoring.status == None:
                scoring = self.invalid_score("""Failed to compute score in SC2B (unknown
                    error). Please contact the organisers provided the submission Id""")


        self.update_submission_status(submission, scoring, production=production)
        self.logger.debug("Exit with status {0}".format(scoring.status))
        return (scoring)

    def score_submission_SCVIS(self, submission, round_number, production=True):
        # "Not yet implemented"
        """ Scores the given submission and returns its status
        """
        # Get the data corresponding to this submission and compute score
        try:
            filename = self.client.getSubmission(submission, downloadFile=True)['filePath']
            scoring = HPNScoring()
            scoring.status = "SCORED"
            scoring.report = ""
            scoring.score = 1
        except:
            filename = "dummy"
            self.logger.debug("1st try block")
            scoring = self.invalid_score("Failed to retrieve submitted file.")
        print filename
        self.update_submission_status(submission, scoring, production=production)
        return (scoring)

    def get_submissions_in_date_range(self, start_date, end_date, sc_index):
        #start_date = dateutil.parser.parse(start_date_string)
        #end_date = dateutil.parser.parse(end_date_string)
        submissions = self.client.getSubmissions(self.evaluationId[sc_index])
        result = {}
        count = 0
        for i, submission in enumerate(submissions):
            count=count+1
            timestamp = dateutil.parser.parse(submission.createdOn)
            if (timestamp>=start_date and timestamp<end_date):
                result[timestamp] = submission
        print("get_submissions_in_date_range: eid="+self.evaluationId[sc_index]+
              ", total count="+str(count)+", # in range="+str(len(result)))
        return (result)
