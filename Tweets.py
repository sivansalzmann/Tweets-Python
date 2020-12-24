#!/usr/bin/env python
# coding: utf-8
import collections

import numpy as np
import pandas as pd
import csv
import re
import datetime



def summary(file_path):
    array = []
    with open(file_path, newline='', encoding='utf-8',errors='ignore') as f:
        reader = csv.DictReader(f, delimiter=';', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        for row in reader:
            array = np.append(array,row)
        return array

def splitHashtag(str):
    btc = re.compile(r'(#bitcoin|#btc|#bitcoins)',re.I)
    x = str.get('text')
    hashtags = np.array(re.findall(r'(?i)\#\w+', x))
    filtered = [i for i in hashtags if not btc.match(i)]
    return filtered


def splitHashtagByMonthMax(array,month,year):
    split =[]
    for i in array:
        x = i.get('timestamp')
        y = datetime.datetime.strptime(x, '%Y-%m-%d %H:%M:%S+%f')
        if y.month == month and y.year == year:
            x = splitHashtag(i)
            split = np.append(split,x,axis=0)

        if split.size != 0:
            maxEle = findMaxHashtag(split)
        else:
            maxEle = "None"

    return maxEle.encode("utf-8")


def findMaxHashtag(npArray):
    l = list()
    for i in npArray:
        l.append(i)
    counter = 0
    ele = l[0]
    for i in l:
        curr_frequency = l.count(i)
        if (curr_frequency > counter):
            counter = curr_frequency
            ele = i
    return ele


def splitUser(str):
    user = re.compile(r'\B\@([\w\-]+)')
    x = str.get('text')
    users = np.array(re.findall(user, x))
    return users


def splitUserByMonthMax(array,month,year):
    split =[]
    maxEle = 0
    for i in array:
        x = i.get('timestamp')
        y = datetime.datetime.strptime(x, '%Y-%m-%d %H:%M:%S+%f')
        if y.month == month and y.year == year:
            x = splitUser(i)
            split = np.append(split,x)
    if split.size != 0:
        maxEle = findMaxUser(split)
    else:
        maxEle = "None"
    return maxEle.encode("utf-8")

def findMaxUser(npArray):
    l = list()
    for i in npArray:
        l.append(i)
    counter = 0
    ele = l[0]
    for i in l:
        curr_frequency = l.count(i)
        if (curr_frequency > counter):
            counter = curr_frequency
            ele = i
    return ele

def splitWeb(npArray):
    webs =[]
    web = re.compile(r'(https?:{1}\/{2}(www\.|[a-zA-Z])+\.com)')
    x = npArray.get('text')
    webs = np.append(webs,re.findall(web, x))
    return webs


def splitWebByMonthMax(array,month,year):
    split =[]
    maxEle = 0
    for i in array:
        x = i.get('timestamp')
        y = datetime.datetime.strptime(x, '%Y-%m-%d %H:%M:%S+%f')
        if y.month == month and y.year == year:
            x = splitWeb(i)
            split = np.append(split,x)
    if split.size != 0:
        maxEle = findMaxWeb(split)
    else:
        maxEle = "None"
    return maxEle

def findMaxWeb(npArray):
    l = list()
    for i in npArray:
        l.append(i)
    del l[1::2]
    counter = 0
    ele = l[0]
    for i in l:
        curr_frequency = l.count(i)
        if (curr_frequency > counter):
            counter = curr_frequency
            ele = i
    return ele

def getTime(row):
    x = row.get('timestamp')
    y = datetime.datetime.strptime(x, '%Y-%m-%d %H:%M:%S+%f')
    return y


def saveToCSV(filePathIn,filePathOut):
    s = summary(filePathIn)
    with open(filePathOut, 'w') as csvFile:
        writer = csv.writer(csvFile, delimiter=",", lineterminator='\n')
        writer.writerow(["Month","Hashtag","Mention","Website"])
        df = pd.DataFrame({"Month":[],"Hashtag":[],"Mention":[],"Website":[]})
        for i in s:
            date = getTime(i)
            dateStr = str(date.year) + "-" + str(date.month)
            # df.insert(0,"Month",dateStr)
            # writer.writerow([str(i),splitHashtagByMonthMax(s,i),splitUserByMonthMax(s,i),splitWebByMonthMax(s,i)])
            # writer.writerow([str(dateStr), splitHashtagByMonthMax(s, date.month,date.year), splitUserByMonthMax(s, date.month,date.year), splitWebByMonthMax(s,date.month,date.year)])
            # df = pd.DataFrame({"Month" : [dateStr]})
            # print(df)
            #print(df.groupby(['Month']).agg(pd.Series.mode))
        #print(df)




x = saveToCSV("Stweets.csv","tweet-data.csv")
#x = summary("Stweets.csv")
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





