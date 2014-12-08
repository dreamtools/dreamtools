# -*- python -*-
#
#  Copyright (c) 2011-2012 - EBI-EMBL
#
#  File author(s): Thomas Cokelaer <cokelaer@ebi.ac.uk>
#
#  Distributed under the GPLv3 License.
#  See accompanying file LICENSE.txt or copy at
#      http://www.gnu.org/licenses/gpl-3.0.html
#
##############################################################################
# This file contains code to generate the pictures shown on 
# http://www.the-dream-project.org/result/information-about-teamsparticipants-dream7
# The module contains the results of the survey monkey 
# http://www.surveymonkey.com/s/8GRVHNW
# It generates 3 plots calle monkey_survey_<tag>.png
from pylab import *

N = 18


#DownloadCreate Chart1. To Which challenge have you participated in ?

Network = 3
NCI = 15


#How many members was your team composed of ?
members = [5,5,2,12,3,3,5,1,1,2,5,1,4,2,3,6,4,2]
assert len(members) == 18
x = hist(members, bins=20)
grid()
xlim([0,max(members)+1])
xlabel("Number of members per team")
ylabel("\#")
ylim([0, max(x[0]+1)])
savefig("monkey_survey_members.png")


# What is/are the background of the team members (several choices possible) ?
background = {
    'Biology':5, 
    'Chemical\nEngineering':2, 
    'Computer\nScience':12,
    'Physics':1,
    'Mathematics':4,
    'Bioinformatics':3,
    'Chemical\nInformatics':1,
    'Statistics':1}

clf()
pie(background.values(), labels=[x + " (%s)"%y for x,y in zip(background.keys(),
background.values())], shadow=True, labeldistance=1.15,
    colors=['y','r','black', 'blue', 'm', 'green', 'orange', 'white', 'cyan'])

savefig("monkey_survey_background.png")

# countries
countries = {
    'Belgium': 1,
    'Finland': 1,
    'France': 1,
    'Germany': 2,
    'Greece': 1,
    'India':2,
    'South Korea': 2,
    'Netherlands':1,
    'United States': 7
}
assert sum(countries.values()) == 18
clf()
pie(countries.values(), labels=[x + " (%s)"%y for x,y in zip(countries.keys(), countries.values())], shadow=True, labeldistance=1.2,
    colors=['y','r','black', 'blue', 'm', 'green', 'orange', 'white', 'cyan'])
savefig("monkey_survey_countries.png")
#pie(countries)

# Do you intend to attend the DREAM7 conference
# (http://www.the-dream-project.org/conferences) ?
dream_participants = {'yes':6, 'no':5, 'dont know':7}
assert sum(dream_participants.values()) == 18

# Do you think that asking for R code instead of the actual prediction is a hurdle ?
R_hurdle = {'yes':9, 'no':9}
assert sum(R_hurdle.values()) == 18

# Do you think that having a challenge with highly unstructured data (many
# variables, missing data as for example real clinical data) hinders
# participation?
unstructured = {'yes':2, 'no': 12, 'somehow':4}
assert sum(unstructured.values()) == 18



