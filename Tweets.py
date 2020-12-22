#!/usr/bin/env python
# coding: utf-8
import numpy as np
import pandas as pd
import csv


# class Tweet:
#     id = 0
#     user = 0
#     fullname = 0
#     url = 0
#     timestemp = 0
#     replies = 0
#     likes = 0
#     retweets = 0
#     text = 0

# my_data = open('Stweets.csv',encoding="utf8").read()
# arr = np.frombuffer(my_data, dtype="<U3")

#npcsv = np.genfromtxt('Stweets.csv', delimiter=';', encoding='utf8',usecols=np.arange(0,1),dtype=str)
npcsv = np.genfromtxt('Stweets.csv', delimiter=';', encoding='utf8',skip_header=10,usecols=np.arange(0,1),dtype=str)
print(npcsv)

# with open("Stweets.csv", "rt") as csvfile:
#     csvreader = csv.reader(csvfile, delimiter=",")
#
#     for row in csvreader:
#         row = [entry.decode("utf8") for entry in row]
#         print(": ".join(row))


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






