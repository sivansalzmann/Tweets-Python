#!/usr/bin/env python
# coding: utf-8
import collections

import numpy as np
import pandas as pd
import csv
import re
import datetime
import time


def findHashtag(string):
    hashTags = np.array([],dtype=str)
    x = re.findall('(#[\w-]+)', string)
    hashTags = np.append(hashTags,x)
    #tags = np.array([],dtype=str)
    tags = ""
    for tag in hashTags:
        if ((tag.lower() != "#btc") and (tag.lower() != "#bitcoin") and (tag.lower() != "#bitcoins")):
            tags += " "
            tags += tag
    return tags

def findUserName(string):
    users = np.array([],dtype=str)
    x = re.findall('(@[^\s]+)', string)
    usersName = np.append(users,x)
    users = ""
    for user in usersName:
        users += user
    return users

def findUrl(string):
    urls = np.array([], dtype=str)
    x = re.findall('http([^\s"]*)://(?P<base>[^/\s]+)', string)
    urlsNames = np.append(urls, x)
    urls = ""
    for url in urlsNames:
        urls += url
    return urls

def summary(filePath):
    arr1 = np.array([],dtype="<U25")
    # hashtags = np.array([],dtype=str)
    btc = re.compile(r'(#bitcoin|#btc|#bitcoins)', re.I)
    with open(filePath, newline='', encoding='utf-8', errors='ignore') as f:
        tweets = csv.DictReader(f, delimiter=';', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        for row in tweets:
            arr = np.array([[str(row.get('timestamp'))],[findHashtag(row.get('text')) + " " +findUserName(row.get('text')) + " " + findUrl(row.get('text'))]],dtype=str)
        #arr1 += arr
        # arr1 = np.append(arr1,arr)
            #print(arr1)
    print(arr1.dtype)
    print(arr.dtype)
    return arr1

x = summary("Stweets.csv")
# def findMaxHashtag(string):
#     l = list()
#     for i in npArray:
#         l.append(i)
#     counter = 0
#     ele = l[0]
#     for i in l:
#         curr_frequency = l.count(i)
#         if (curr_frequency > counter):
#             counter = curr_frequency
#             ele = i
#     return ele
#
#
# def splitUser(str):
#     user = re.compile(r'\B\@([\w\-]+)')
#     x = str.get('text')
#     users = np.array(re.findall(user, x))
#     return users
#
#
# def splitUserByMonthMax(array,month,year):
#     split =[]
#     maxEle = 0
#     for i in array:
#         x = i.get('timestamp')
#         y = datetime.datetime.strptime(x, '%Y-%m-%d %H:%M:%S+%f')
#         if y.month == month and y.year == year:
#             x = splitUser(i)
#             split = np.append(split,x)
#     if split.size != 0:
#         maxEle = findMaxUser(split)
#     else:
#         maxEle = "None"
#     return maxEle.encode("utf-8")
#
# def findMaxUser(npArray):
#     l = list()
#     for i in npArray:
#         l.append(i)
#     counter = 0
#     ele = l[0]
#     for i in l:
#         curr_frequency = l.count(i)
#         if (curr_frequency > counter):
#             counter = curr_frequency
#             ele = i
#     return ele
#
# def splitWeb(npArray):
#     webs =[]
#     web = re.compile(r'(https?:{1}\/{2}(www\.|[a-zA-Z])+\.com)')
#     x = npArray.get('text')
#     webs = np.append(webs,re.findall(web, x))
#     return webs
#
#
# def splitWebByMonthMax(array,month,year):
#     split =[]
#     maxEle = 0
#     for i in array:
#         x = i.get('timestamp')
#         y = datetime.datetime.strptime(x, '%Y-%m-%d %H:%M:%S+%f')
#         if y.month == month and y.year == year:
#             x = splitWeb(i)
#             split = np.append(split,x)
#     if split.size != 0:
#         maxEle = findMaxWeb(split)
#     else:
#         maxEle = "None"
#     return maxEle
#
# def findMaxWeb(npArray):
#     l = list()
#     for i in npArray:
#         l.append(i)
#     del l[1::2]
#     counter = 0
#     ele = l[0]
#     for i in l:
#         curr_frequency = l.count(i)
#         if (curr_frequency > counter):
#             counter = curr_frequency
#             ele = i
#     return ele
#
# def getTime(row):
#     x = row.get('timestamp')
#     y = datetime.datetime.strptime(x, '%Y-%m-%d %H:%M:%S+%f')
#     return y
#
#
def saveToCSV(filePathIn,filePathOut):
    s = summary(filePathIn)
    with open(filePathOut, 'w') as csvFile:
        writer = csv.writer(csvFile, delimiter=",", lineterminator='\n')
        writer.writerow(["Month","Hashtag","Mention","Website"])
        for i in s:
            print(i)
            dateStr = str(date.year) + "-" + str(date.month)
            # df.insert(0,"Month",dateStr)
            # writer.writerow([str(i),splitHashtagByMonthMax(s,i),splitUserByMonthMax(s,i),splitWebByMonthMax(s,i)])
            # writer.writerow([str(dateStr), splitHashtagByMonthMax(s, date.month,date.year), splitUserByMonthMax(s, date.month,date.year), splitWebByMonthMax(s,date.month,date.year)])
            # df = pd.DataFrame({"Month" : [dateStr]})
            # print(df)
            #print(df.groupby(['Month']).agg(pd.Series.mode))
        #print(df)
#
#
#
# x = summary("Stweets.csv")
# x = saveToCSV("Stweets.csv","tweet-data.csv")
# start_time = time.time()
# x = summary("Stweets.csv")
# print("--- %s seconds ---" % (time.time() - start_time))

#print(x)
#getTime(x)
# for i in x:
#     print(i)
#     getTime(x)
# y = splitUserByMonthMax(x,10,2017)
# print(y)
#y = splitWebByMonthMax(x,5,2018)
#print(splitToMonthesreturnMax(x,4))
#print(vaildHashtag(x))
#splitHashtag(x)
#findMaxHashtag(y)
#print(splitWeb(x))
#print(splitWebByMonthMax(x,6))





