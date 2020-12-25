import re
import numpy as np
import csv
import time


def findMax(dates, name):
    if bool(dates[name]):
        max = 0
        maxVal = "None"
        for k, v in dates[name].items():
            if v > max:
                max = v
                maxVal = k
        return maxVal
    else:
        return "None"


def countTimes(data, nameOfCat, reStatments):
    for i in reStatments:
        if nameOfCat == "webs":
            string = i.group(1)
        else:
            string = i.group()
        if nameOfCat == "hashTags":
            check = string[1:].lower()
            if check == "bitcoin" or check == "bitcoins" or check == "btc":
                continue
        if data[nameOfCat].get(string) == None:
            data[nameOfCat].update({string: 1})
        else:
            data[nameOfCat][string] += 1


def saveSummary(filePath, dictDates, listDates):
    try:
        with open(filePath, "w", encoding='utf8') as csvFile:
            csvFile.write("Month,Hashtag,Mention,Website\n")
            dateNpArray = np.array(listDates)
            dateNpArray.sort()
            for date in dateNpArray:
                csvFile.write(date)
                csvFile.write(",")
                csvFile.write(findMax(dictDates[date], "hashTags"))
                csvFile.write(",")
                csvFile.write(findMax(dictDates[date], "mentions"))
                csvFile.write(",")
                csvFile.write(findMax(dictDates[date], "webs"))
                csvFile.write("\n")
    except:
        print("Error-The file path is not vaild")


def summary(filePath):
    try:
        dataDict = {}
        listDates = []
        hash = "#([\w-]+)"
        ment = "@[\w-]+"
        web = "https*://([^/\s]*)"
        with open(filePath, "r", encoding='utf8', errors='ignore') as read_file:
            tweets = csv.DictReader(read_file, delimiter=';')
            for row in tweets:
                tweet = dict(row)["timestamp"][:7]
                hashTags = re.finditer(hash, dict(row)["text"])
                mentions = re.finditer(ment, dict(row)["text"])
                webs = re.finditer(web, dict(row)["text"])
                if dataDict.get(tweet) == None:
                    listDates.append(tweet)
                    hashTagDict = {}
                    mentionsDict = {}
                    websDict = {}
                    dataDict.update({tweet: {"hashTags": hashTagDict, "mentions": mentionsDict, "webs": websDict}})
                countTimes(dataDict[tweet], "hashTags", hashTags)
                countTimes(dataDict[tweet], "mentions", mentions)
                countTimes(dataDict[tweet], "webs", webs)
        return dataDict, listDates
    except:
        print("Error-The file path is not vaild")


if __name__ == "__main__":
    start_time = time.time()
    dataDict, listDates = summary("tweets.csv")
    saveSummary("tweet-data.csv", dataDict, listDates)
    print("--- %s seconds ---" % (time.time() - start_time))
