import datetime as dt 
import pandas as pd 
import csv
import xlrd
import string


#OUT_FILE = "/Users/Kasdan/Desktop/filtered_trump_tweets.csv"

workbook = xlrd.open_workbook('excelFiles/trump_tweets.xlsx', {'default_date_format': 'mm/dd/yy'})
sh = workbook.sheet_by_index(0)

#words = ["media", "news", "nyt", "cbs", "fox", "nbc"]



def datesAreEqual(date1, date2):
    dLen1 = len(date1)
    dLen2 = len(date2)
    if(dLen1 != dLen2): return False
    for i in range(dLen1):
        if(date1[i] != date2[i]): return False
    return True



for i in range(1,15025):
    tweet = sh.cell(i,0).value
    for l in tweet:
        if(ord(l) > 126 or ord(l) < 32):
            tweet = tweet.replace(l,"")
    tweetL = tweet.lower()
    


    if("media" in tweetL or "news" in tweetL or "nyt" in tweetL or 
        "cbs" in tweetL or "fox" in tweetL or "nbc" in tweetL or 
        "fake" in tweetL):
        
        dates = sh.cell(i, 1).value
        if(isinstance(dates, int) or isinstance(dates,float)):
            year, month, day, hour, minute, second = xlrd.xldate_as_tuple(dates, workbook.datemode)
            dates = str(month)+'/'+str(day)+'/'+str(year)


        if(i < 15024):
            nextDate = sh.cell(i+1, 1).value
            if(isinstance(nextDate, int) or isinstance(nextDate,float)):
                year1, month1, day1, hour1, minute1, second1 = xlrd.xldate_as_tuple(nextDate, workbook.datemode)
                nextDate = str(month1)+'/'+str(day1)+'/'+str(year1)
        
        favs = sh.cell(i, 2).value
        rts = sh.cell(i, 3).value
        #print(dates)
        #print(nextDate)
        #if(datesAreEqual(dates, nextDate)): print("they are equal")
        # print(favs)
        # print(rts)

        # with open('filtered_trump_tweets.csv', 'a', newline='') as csvfile:
        #     tweetwriter = csv.writer(csvfile)
        #     tweetwriter.writerow([tweet,dates,favs,rts])
        # csvfile.close()










