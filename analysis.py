##################################
#IMPORTS
##################################
import csv
import scipy
import numpy as np
from scipy import stats
from datetime import datetime
import pandas as pd 
import pandas_datareader.data as web
import matplotlib.pyplot as plt 
from matplotlib import style
import math


##################################
#COLLECT ALL THE DATA ABOUT TWEETS
##################################
with open('filtered_trump_tweets.csv') as csvfile:
    readCSV = csv.reader(csvfile, delimiter=',')

    tweetsArr = []
    
    tweetD = {}  #THIS HOLDS THE DATE AND THE TWEET SCORE OF THAT DAY
    for row in readCSV:

        tweetsArr.append(row)

        row[0] = datetime.strptime(row[0], '%m/%d/%y')
        #ADD UP THE SCORE -> NUMBER OF FAVS + 3 * NUMBER OF RTS
        if(row[0] not in tweetD): tweetD[row[0]] = 0 + (int(row[2]) + (3*int(row[3])))

        else: tweetD[row[0]] = tweetD[row[0]] + (int(row[2]) + (3*int(row[3])))

csvfile.close()

######################################
# FIND AVERAGE TWEET SCORE FOR A DAY #
######################################
total = 0
count = 0

for key in tweetD:
    total += tweetD[key]
    count += 1

avg = total/count   #AVERAGE TWEET SCORE = 126342.8538961039



#######################################################
#CUTS OUT ALL OF THE DAYS LESS THAN AVERAGE TWEET SCORE
#######################################################
def removeLowerThanAvg(tweetD, avg):

    newTweetD = {}
    for key in tweetD:
        if(tweetD[key] > avg): newTweetD[key] = tweetD[key]
    return newTweetD
        
newTweetD = removeLowerThanAvg(tweetD, avg) #FILTERED TWEETS


#######################################################
#   GET INDIVIDUAL LISTS OF ALL TWEETS FOR COMPANIES  #
#######################################################

def tweetsNYT(tweets):
    nytArr = []
    for tweet in tweets:
        tweetL = tweet[1].lower()
        if("@nytimes" in tweetL or "new york times" in tweetL or "NY Times" in tweet[1]):
            nytArr.append(tweet)
    return nytArr

def tweetsCMCSA(tweets):
    nbcArr = []
    for tweet in tweets:
        if("nbc" in tweet[1].lower()):
            nbcArr.append(tweet)
    return nbcArr

def tweetsCBS(tweets):
    cbsArr = []
    for tweet in tweets:
        if("cbs" in tweet[1].lower()):
            cbsArr.append(tweet)
    return cbsArr

def tweetsFOX(tweets):
    foxArr = []
    for tweet in tweets:
        if("fox" in tweet[1].lower()):
            foxArr.append(tweet)
    return foxArr

def tweetsBAD(tweets):
    badArr = []
    for tweet in tweets:
        tweet = tweet[1].lower()
        if("bad" in tweet or "fail" in tweet or "fake" in tweet or "wrong" in tweet or "loser" in tweet):
            badArr.append(tweet)



######################################################################
#                       DATA FROM NYT.CSV STOCK                      #
######################################################################


with open('excelFiles/NYT.csv') as csvfileNYT:
    readCSV = csv.reader(csvfileNYT, delimiter=',')

    dailyDiffNYT = {} #HOLDS DATE AND HIGH-LOW
    lol = False
    for rowNYT in readCSV:
        #CONVERTS STRING DATES TO DATETIMES
        if(lol == True): 
            rowNYT[0] = datetime.strptime(rowNYT[0], '%m/%d/%y')
            dailyDiffNYT[rowNYT[0]] = float(rowNYT[6]) #BY VOLUME THAT DAY
            #dailyDiffNYT[rowNYT[0]] = (float(rowNYT[1]) - float(rowNYT[4]))
            #CURRENTLY CHECKS OPEN - CLOSE
        lol = True

csvfileNYT.close()


######################################################################
#                       DATA FROM NBC.CSV STOCK                      #
######################################################################


with open('excelFiles/CMCSA.csv') as csvfileNBC:
    readCSV = csv.reader(csvfileNBC, delimiter=',')

    dailyDiffNBC = {} #HOLDS DATE AND HIGH-LOW
    lol = False
    for rowNBC in readCSV:
        #CONVERTS STRING DATES TO DATETIMES
        if(lol == True): 
            rowNBC[0] = datetime.strptime(rowNBC[0], '%Y-%m-%d')
            dailyDiffNBC[rowNBC[0]] = float(rowNBC[6]) #BY VOLUME THAT DAY
            #dailyDiffNBC[rowNBC[0]] = (float(rowNBC[1]) - float(rowNBC[4]))
            #CURRENTLY CHECKS OPEN - CLOSE
        lol = True

csvfileNBC.close()



######################################################################
#                       DATA FROM CBS.CSV STOCK                      #
######################################################################


with open('excelFiles/CBS.csv') as csvfileCBS:
    readCSV = csv.reader(csvfileCBS, delimiter=',')

    dailyDiffCBS = {} #HOLDS DATE AND HIGH-LOW
    lol = False
    for rowCBS in readCSV:
        #CONVERTS STRING DATES TO DATETIMES
        if(lol == True): 
            rowCBS[0] = datetime.strptime(rowCBS[0], '%Y-%m-%d')
            dailyDiffCBS[rowCBS[0]] = float(rowCBS[6]) #BY VOLUME THAT DAY
            #dailyDiffCBS[rowCBS[0]] = (float(rowCBS[1]) - float(rowCBS[4]))
            #CURRENTLY CHECKS OPEN - CLOSE
        lol = True

csvfileCBS.close()


######################################################################
#                       DATA FROM FOX.CSV STOCK                      #
######################################################################


with open('excelFiles/FOX.csv') as csvfileFOX:
    readCSV = csv.reader(csvfileFOX, delimiter=',')

    dailyDiffFOX = {} #HOLDS DATE AND HIGH-LOW
    lol = False
    for rowFOX in readCSV:
        #CONVERTS STRING DATES TO DATETIMES
        if(lol == True): 
            rowFOX[0] = datetime.strptime(rowFOX[0], '%Y-%m-%d')
            dailyDiffFOX[rowFOX[0]] = float(rowFOX[6]) #BY VOLUME THAT DAY
            #dailyDiffFOX[rowFOX[0]] = (float(rowFOX[1]) - float(rowFOX[4]))
            #CURRENTLY CHECKS OPEN - CLOSE
        lol = True

csvfileFOX.close()








def tweetScore(tweet):
    return int(tweet[2]) + 3*int(tweet[3])


def dailyTweetScore(tweets):
    tweetScores = {}
    lol = False
    for row in tweets:
        if(lol == True):
            if(row[0] not in tweets): tweetScores[row[0]] = 0 + (int(row[2]) + (3*int(row[3])))
            else: tweetScores[row[0]] = tweetScores[row[0]] + (int(row[2]) + (3*int(row[3])))
        lol = True
    return tweetScores








#####################################################################
#####################################################################
#                PART FOR GRAPHING THE RELATIONSHIPS                #
#####################################################################
#####################################################################


################################################################################
#CREATE A LIST OF DATES AND TWEET SCORES FOR ALL TWEETS (GENERAL)->CAN SEE RISE#
#AROUND TIME HE WAS NOMINATED                                                  #
################################################################################

#FIND WHAT THE SPIKE WAS

dates = []
tweetScore = []

for key in tweetD:
    dates.append(key)
    tweetScore.append(tweetD[key])

#REVERSE DATA SO IT MAKES SENSE GOING FORWARD
dates = dates[::-1]
tweetScore = tweetScore[::-1]
print(tweetScore[tweetScore.index(max(tweetScore))])
print(dates[tweetScore.index(max(tweetScore))])

#GRAPHS THE GENERAL DATA FOR ALL TWEETS
ts = pd.Series(tweetScore, dates)
ts.plot()
plt.xlabel("Dates")
plt.ylabel("Daily Tweet Score")
plt.title("Date vs. Daily Tweet Score")
plt.show()



##############################
#       GRAPH FOR NYT        #
##############################
nytTweets = tweetsNYT(tweetsArr)
xNYT = []
yNYT = []

tweetScoresNYT = dailyTweetScore(nytTweets)

for date in tweetScoresNYT:
    if(date in dailyDiffNYT):
    #CHECKS IF DATE OF TWEET IS IN THE STOCK DATA
        xNYT.append(tweetScoresNYT[date])
        yNYT.append(dailyDiffNYT[date])

plt.scatter(xNYT, yNYT)
plt.plot(np.unique(xNYT), np.poly1d(np.polyfit(xNYT, yNYT, 1))(np.unique(xNYT)))
print("Pearson Correlation Coefficient NYT: ",scipy.stats.pearsonr(xNYT, yNYT)[0])
plt.xlabel("Daily Tweet Score")
plt.ylabel("Daily NYT Stock Volume")
plt.title("Daily Tweet Score vs. NYT Stock Volume")
plt.show()

#FIND THE THREE OUTLIERS FOR TWEET SCORE AND DIFF INDIVIDUALLY


##############################
#       GRAPH FOR NBC        #
##############################
nbcTweets = tweetsCMCSA(tweetsArr)
xNBC = []
yNBC = []

tweetScoresNBC = dailyTweetScore(nbcTweets)

for date in tweetScoresNBC:
    if(date in dailyDiffNBC):
    #CHECKS IF DATE OF TWEET IS IN THE STOCK DATA
        xNBC.append(tweetScoresNBC[date])
        yNBC.append(dailyDiffNBC[date])

plt.scatter(xNBC, yNBC)
plt.plot(np.unique(xNBC), np.poly1d(np.polyfit(xNBC, yNBC, 1))(np.unique(xNBC)))
print("Pearson Correlation Coefficient NBC: ",scipy.stats.pearsonr(xNBC, yNBC)[0])
plt.xlabel("Daily Tweet Score")
plt.ylabel("Daily NBC Stock Volume")
plt.title("Daily Tweet Score vs. NBC Stock Volume")
plt.show()



##############################
#       GRAPH FOR CBS        #
##############################
cbsTweets = tweetsCBS(tweetsArr)
xCBS = []
yCBS = []

tweetScoresCBS = dailyTweetScore(cbsTweets)

for date in tweetScoresCBS:
    if(date in dailyDiffCBS):
    #CHECKS IF DATE OF TWEET IS IN THE STOCK DATA
        xCBS.append(tweetScoresCBS[date])
        yCBS.append(dailyDiffCBS[date])

plt.scatter(xCBS, yCBS)
plt.plot(np.unique(xCBS), np.poly1d(np.polyfit(xCBS, yCBS, 1))(np.unique(xCBS)))
print("Pearson Correlation Coefficient CBS: ",scipy.stats.pearsonr(xCBS, yCBS)[0])
plt.xlabel("Daily Tweet Score")
plt.ylabel("Daily CBS Stock Volume")
plt.title("Daily Tweet Score vs. CBS Stock Volume")
plt.show()


##############################
#       GRAPH FOR FOX        #
##############################
foxTweets = tweetsFOX(tweetsArr)
xFOX = []
yFOX = []

tweetScoresFOX = dailyTweetScore(foxTweets)

for date in tweetScoresFOX:
    if(date in dailyDiffFOX):
    #CHECKS IF DATE OF TWEET IS IN THE STOCK DATA
        xFOX.append(tweetScoresFOX[date])
        yFOX.append(dailyDiffFOX[date])



plt.scatter(xFOX, yFOX)
plt.plot(np.unique(xFOX), np.poly1d(np.polyfit(xFOX, yFOX, 1))(np.unique(xFOX)))
print("Pearson Correlation Coefficient FOX: ",scipy.stats.pearsonr(xFOX, yFOX)[0])
plt.xlabel("Daily Tweet Score")
plt.ylabel("Daily FOX Stock Volume")
plt.title("Daily Tweet Score vs. FOX Stock Volume")
plt.show()


