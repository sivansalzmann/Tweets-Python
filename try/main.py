#!/usr/bin/env python
# coding: utf-8
import collections

import numpy as np
import pandas as pd
import csv
import re
import datetime
import time
import operator


def summary(filePath):

    tweets = {'timetamp':[],'hashtags':[],'mentions':[],'urls':[]}
    has = re.compile(r'(#[\w-]+)')
    men = re.compile(r'(@[^\s]+)')
    url = re.compile(r'http([^\s"]*)://(?P<base>[^/\s]+)')

    with open(filePath, newline='', encoding='utf-8', errors='ignore') as f:
        reader = csv.DictReader(f, delimiter=';', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        for row in reader:
            # x = row['timestamp']
            # date = datetime.datetime.strptime(x, '%Y-%m-%d %H:%M:%S+%f')
            # dateStr = str(date.year) + "-" + str(date.month)
            tweets['timetamp'].append(row['timestamp'])
            tweets['hashtags'].append(re.findall(has,row['text']))
            tweets['mentions'].append(re.findall(men, row['text']))
            tweets['urls'].append(re.findall(url, row['text']))
    return tweets
    # print(tweet['timetamp'][0])
    # print(tweet['hashtags'][0])
    # print(tweet['mentions'][0])
    # print(tweet['urls'][0])

def makeToghter(tweets):
    pass
    #print(tweets)
    # for i in range(len(tweets["timetamp"])):
    #     #print(i)
    #     key = tweets["timetamp"][i]
    #     if tweets["hashtags"][i] != None:



# def saveSummary(fiePathOut,tweets):
#     tweetsToCsv = {'Month':[],'hashtags':[],'mentions':[],'urls':[]}
#     with open(fiePathOut, "w", newline='', encoding='utf-8') as file:
#         hedars = ["Month", "Hashtag", "Mention", "Website"]
#         writer = csv.DictWriter(file, hedars)
#         writer.writeheader()
#
#         for i in range(len(tweets["timetamp"])):
#             key = tweets["timetamp"][i]
#             tweetsToCsv["Month"] = key
#             #print(tweetsToCsv)
#             if tweets["timetamp"][i] == key:
#                 # tweetsToCsv["hashtags"].append()
#                 #print(i)
#                 #print("ok")
#                 #tmpMode["Hashtag"] = pd.Series.mode(tmpDict[key]["tags"]).iloc[0]
#             # else:
#             #     tmpMode["Hashtag"] = ("None")
#             # if tmpDict[key]["names"]:
#             #     tmpMode["Mention"] = pd.Series.mode(tmpDict[key]["names"]).iloc[0]
#             # else:
#             #     tmpMode["Mention"] = ("None")
#             # if tmpDict[key]["urls"]:
#             #     tmpMode["Website"] = pd.Series.mode(tmpDict[key]["urls"]).iloc[0]
#             # else:
#             #     tmpMode["Website"] = ("None")
#             # writer.writerow(tmpMode)
#     #print(tweetsToCsv)

start_time = time.time()
x = summary("tweets.csv")
#y = makeToghter(x)
#saveSummary("tweet-data.csv",x)
print("--- %s seconds ---" % (time.time() - start_time))