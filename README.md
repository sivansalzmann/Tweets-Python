# Tweets-Python

Twitter tweets can hold a mountain of information, however sifting through the texts can be an ordeal.
For this exercise, you will work with a CSV file containing meta-data and texts of tweets regarding the
topic of Bitcoin over the last few years.

- install the package pip install numpy
- The source CSV file will be named “tweets.csv”.
- The output CSV file will be named “tweet-data.csv”.
- The source file will be in utf-8 encoding and must be saved in the same encoding.
- Each row in the output CSV will be one month (e.g. 2013-02, 2014-01, …).

## Run time isuue
The program was designed to be executed with maximum efficiency.

## Input
- The most used ‘hashtag’ (#<tag>) of the month (not including #bitcoin, #bitcoins or #btc with
  any capitalization – e.g. #BTC, #BITcoin, …)
- The most mentioned username (@<username>) of the month
- The most referenced website (http or https) of the month

The data set will be saved in a CSV file with the following headers: Month,Hashtag,Mention,Website
 
