#!/usr/bin/env python3

"""
Cronjob in a script: https://www.baeldung.com/linux/create-crontab-script
Online cronjob time: https://crontab.guru/every-day-at-midnight
"""

from os import system as cmd
from requests import get
from bs4 import BeautifulSoup as bs
from datetime import datetime as dt
#Global constat variables
PRAYERS = {'fajr', 'sunrise', 'dhuhr', 'asr', 'maghrib', 'isha'}
#Global normal variables
url = "https://www.google.com/search?q=prayer+time++&source=hp&ei=dPu0Y8LdCfSf5NoPgKmG8Ag&iflsig=AJiK0e8AAAAAY7UJhIK5FOlaeDutOWF0nQRK8RVecKmM&ved=0ahUKEwjC54SPha38AhX0D1kFHYCUAY4Q4dUDCAs&uact=5&oq=prayer+time++&gs_lcp=Cgdnd3Mtd2l6EAMyBggAEBYQHjoUCC4QjwEQxwEQ0QMQ6gIQjAMQ5QI6DgguEI8BEOoCEIwDEOUCOg4IABCPARDqAhCMAxDlAjoLCC4QgAQQxwEQ0QM6CwgAEIAEELEDEIMBOggIABCABBCxAzoLCC4QgAQQsQMQgwE6EQguEIAEELEDEIMBEMcBENEDOg4ILhCABBCxAxDHARDRAzoLCC4QgAQQxwEQrwE6BQgAEIAEOggILhCABBDUAjoICAAQsQMQgwE6EQguEIAEELEDEMcBENEDENQCOgQIABADOggILhCABBCxAzoFCC4QgAQ6DggAEIAEELEDEIMBEMkDOgsILhCABBCxAxDUAjoOCC4QgAQQsQMQgwEQ1AI6CAgAEIAEEMkDOggIABAWEB4QDzoFCAAQhgM6BQghEKABOgUIIRCrAlCHCFjfJWDFJ2gCcAB4AIABbIgB_AqSAQQyMS4xmAEAoAEBsAEK&sclient=gws-wiz"

def convTimeToCronStr(prayer:str, time:str):
    cronTime = dt.strptime(time, '%I:%M:%S %p').strftime('%H:%M:%S')
    cronTime = cronTime.split(":")
    cronstring = f"{cronTime[1]} {cronTime[0]} * * * mpg123 /home/student/Code/"
    if prayer == "fajr":  
        cronstring += 'azan.mp3'
    else:
        cronstring += 'azan.mp3'
    return cronstring

def responseParser():
    """
    Parse through the html code for the necessary informations
    Returns
    -------
    str
        the needed information from the html code
    """
    global url, PRAYERS
    maxCount = 11
    count = 0
    prayerName = ''
    prayerTime = ''
    prayerTimeClass = ["r0bn4c", "rQMQod"] #file for prayer time
    httpResponse = get(url).text #HTTP GET
    tree = bs(httpResponse, 'html.parser')
    prayerNameAndTime = dict()
    
    for span in tree.find_all('span'):
        if span.get('class') != None:
            try:
                content = span.contents[0].lower()
                currClasss = span.get('class')
                if content in PRAYERS or currClasss == prayerTimeClass and count <= maxCount:
                    if count % 2 == 0:
                        prayerName = str(content).capitalize()
                    else:
                        prayerTime = str(content)
                        prayerTime = prayerTime.replace("\u202f", ":00 ")
                        prayerNameAndTime[prayerName] = prayerTime
                    count += 1
            except:
                continue

    return prayerNameAndTime

def makeCronJob(prayerAndTime):
    cmd("crontab -r")
    cmd("touch prayer_cronjob_file.txt")
    defaultCronJob = "0 0 * * * /home/student/Code/prayerTime.py"
    cmd(f'echo "{defaultCronJob}" > prayer_cronjob_file.txt')
    for key in prayerAndTime:
        if key.lower() != "sunrise":
            cronString = convTimeToCronStr(key,prayerAndTime[key])
            cmd(f'echo "{cronString}" >> prayer_cronjob_file.txt')
            cmd("crontab prayer_cronjob_file.txt")
    cmd("rm -f prayer_cronjob_file.txt")

def main():
    myPrayers = responseParser()
    makeCronJob(myPrayers)

if __name__ == '__main__':
    main()
