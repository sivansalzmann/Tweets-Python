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
    hashtags = list()
    x = str.get('text')
    hashtags.append(re.findall(r'(?i)\#\w+', x))
    for j in hashtags:
        filtered = [i for i in j if not btc.match(i)]
    return filtered


def splitAndFindMax(array,month):
    l = list()
    maxList = list()
    for i in array:
        x = i.get('timestamp')
        y = datetime.datetime.strptime(x, '%Y-%m-%d %H:%M:%S+%f')
        if y.month == month:
            l.append(splitHashtag(i))
    maxList.append(findMaxHashtag(l))
    return maxList


def findMaxHashtag(l):
    newL = list()
    for i in l:
        for j in i:
            newL.append(j)
    counter = 0
    num = newL[0]
    for i in newL:
        curr_frequency = newL.count(i)
        if (curr_frequency > counter):
            counter = curr_frequency
            num = i
    return num

def findMaxUser(l):
    newL = list()
    for i in l:
        for j in i:
            newL.append(j)
    counter = 0
    num = newL[0]
    for i in newL:
        curr_frequency = newL.count(i)
        if (curr_frequency > counter):
            counter = curr_frequency
            num = i
    return num

def saveToCSV(fiePathIn,filePathOut):
    s = summary(fiePathIn)
    with open(filePathOut, 'w') as csvFile:
        writer = csv.writer(csvFile, delimiter=",", lineterminator='\n')
        writer.writerow(["Month","Hashtag","Mention","Website"])
        for i in range(1,13):
            writer.writerow([str(i),splitAndFindMax(s,i)])




x = saveToCSV("Stweets.csv","tweet-data.csv")
#splitToMonthes(x)
#print(splitToMonthesreturnMax(x,4))
#print(vaildHashtag(x))
#splitHashtag(x)



    # def __init__(self):
    #     #constractur
    #
    # def setTweets(self):
    #
    # def getId(self):
    #
    # def getUser(self):
    #
    # def getFullname(self):
    #
    # def getUrl(self):
    #
    # def getTimestemp(self):
    #
    # def getReplies(self):
    #
    # def getLikes(self):
    #
    # def getRetweets(self):
    #
    # def getText(self):
    #
    # #first task
    # def textOfMonth(self):
    #
    # def findSigns(self,sign): #uses for hashtag and website
    #
    # def hashtagValidation(self):
    #
    # def mostUsedHahtags(self): #dont forget add symbol
    #
    # #second task
    # def usersOfMonth(self):
    #
    # def usernameValisation(self):
    #
    # def mostMentionUsername(self): #dont forget add symbol
    #
    # #third task
    # def websiteOfMonth(self):
    #
    # def websiteValisation(self):
    #
    # def mostMentionWebsite(self): #dont forget remove things
    #
    # def dateFormat(self): #help to save to csv just month wnd year
    #
    # def checkRowValidation(self): # put value None
    #
    # def saveToCsv(self): #save res to csv






