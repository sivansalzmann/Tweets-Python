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


def splitHashtagByMonthMax(array,month):
    split =[]
    for i in array:
        x = i.get('timestamp')
        y = datetime.datetime.strptime(x, '%Y-%m-%d %H:%M:%S+%f')
        if y.month == month:
            x = splitHashtag(i)
            split = np.append(split,x,axis=0)
    maxEle = findMaxHashtag(split)
    return maxEle



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
    for i in str:
        users = np.array(str.get('user'))
    return users


def splitUserByMonthMax(array,month):
    split =[]
    for i in array:
        x = i.get('timestamp')
        y = datetime.datetime.strptime(x, '%Y-%m-%d %H:%M:%S+%f')
        if y.month == month:
            x = splitUser(i)
            #print(x)
            split = np.append(split,x)
    maxEle = findMaxUser(split)
    return maxEle

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


def splitWebByMonthMax(array,month):
    split =[]
    maxEle = 0
    for i in array:
        x = i.get('timestamp')
        y = datetime.datetime.strptime(x, '%Y-%m-%d %H:%M:%S+%f')
        if y.month == month:
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


def saveToCSV(fiePathIn,filePathOut):
    s = summary(fiePathIn)
    with open(filePathOut, 'w') as csvFile:
        writer = csv.writer(csvFile, delimiter=",", lineterminator='\n')
        writer.writerow(["Month","Hashtag","Mention","Website"])
        for i in range(1,13):
            writer.writerow([str(i),splitHashtagByMonthMax(s,i),splitUserByMonthMax(s,i),splitWebByMonthMax(s,i)])




x = saveToCSV("Stweets.csv","tweet-data.csv")
#x = summary("Stweets.csv")
# y = splitUserByMonthMax(x,5)
#y = splitByMonth(x,5)
#print(splitToMonthesreturnMax(x,4))
#print(vaildHashtag(x))
#splitHashtag(x)
#findMaxHashtag(y)
#print(splitWeb(x))
#print(splitWebByMonthMax(x,6))



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






