import re
import numpy as np
import csv


def findMax(dates, name):
    """
    This function return the max shown value in category by date
    :param dates:
    :param name:
    :return: maxVal and None if there isn`t good data in the date
    """
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
    """
    :param data:
    :param nameOfCat:
    :param reStatments:
    """
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


def saveSummary(filePathIn,filePathOut):
    """
    This function save the results of the required functions to new CSV file called tweet-data.csv
    :param filePathIn:
    :param filePathOut:
    """
    dictDates, listDates = summary(filePathIn)
    with open(filePathOut, "w", encoding='utf8') as csvFile:
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


def summary(filePath):
    """
    This function read data from csv file called tweets.csv and separate the data to by the specific instructions:
    hashTags
    mentions
    webs
    :param filePath:
    :return: dataDict, listDates
    """
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


if __name__ == "__main__":
    saveSummary("tweets.csv","tweet-data.csv")
