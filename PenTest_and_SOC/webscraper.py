#!/usr/bin/env python

"""
Name: Miftahul Huq
Date: 08/28/2022
Course: CSEC 380 (Prin of Web App Security)
Instructor: Rob Olson
"""
import re
import os
import sys
import whois
import requests as req
import multiprocessing as mp
from curses.ascii import isdigit
from bs4 import BeautifulSoup as bs

urlRegexRule = r"\b((?:https?://)?(?:(?:www\.)?(?:[\da-z\.-]+)\.(?:[a-z]{2,6})|(?:(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.)\{3}(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)|(?:(?:[0-9a-fA-F]{1,4}:){7,7}[0-9a-fA-F]{1,4}|(?:[0-9a-fA-F]{1,4}:){1,7}:|(?:[0-9a-fA-F]{1,4}:){1,6}:[0-9a-fA-F]{1,4}|(?:[0-9a-fA-F]{1,4}:){1,5}(?::[0-9a-fA-F]{1,4}){1,2}|(?:[0-9a-fA-F]{1,4}:){1,4}(?::[0-9a-fA-F]{1,4}){1,3}|(?:[0-9a-fA-F]{1,4}:){1,3}(?::[0-9a-fA-F]{1,4}){1,4}|(?:[0-9a-fA-F]{1,4}:){1,2}(?::[0-9a-fA-F]{1,4}){1,5}|[0-9a-fA-F]{1,4}:(?:(?::[0-9a-fA-F]{1,4}){1,6})|:(?:(?::[0-9a-fA-F]{1,4}){1,7}|:)|fe80:(?::[0-9a-fA-F]{0,4}){0,4}%[0-9a-zA-Z]{1,}|::(?:ffff(?::0{1,4}){0,1}:){0,1}(?:(?:25[0-5]|(?:2[0-4]|1{0,1}[0-9]){0,1}[0-9])\.){3,3}(?:25[0-5]|(?:2[0-4]|1{0,1}[0-9]){0,1}[0-9])|(?:[0-9a-fA-F]{1,4}:){1,4}:(?:(?:25[0-5]|(?:2[0-4]|1{0,1}[0-9]){0,1}[0-9])\.){3,3}(?:25[0-5]|(?:2[0-4]|1{0,1}[0-9]){0,1}[0-9])))(?::[0-9]{1,4}|[1-5][0-9]{4}|6[0-4][0-9]{3}|65[0-4][0-9]{2}|655[0-2][0-9]|6553[0-5])?(?:/[\w\.-]*)*/?)\b"
isDepthZero = True
linkDepth = dict()
process_queue = mp.Queue()
process_queue.put(linkDepth)
process_queue.put(isDepthZero)
process_queue.put(urlRegexRule)

def check_parameters(parameters):
    paramLen = len(parameters)
    validParamNum = True if paramLen == 3 else False
    validDomain = False
    if paramLen != 0:
        try:
            w = whois.whois(parameters[0])
        except Exception:
            validDomain = False
        else:
            validDomain = True
    try:
        validURL = True if paramLen >= 2 and req.get("http://"+parameters[1]).status_code == 200 else False
    except:
        validURL = False
    try:
        validDepth = True if validParamNum and isdigit(parameters[2]) else False
    except:
        validDepth = False
    allValidParam = True if validParamNum and validDomain and validURL and validDepth else False

    if paramLen != 0:
        if not allValidParam:
            print("""
            \rERROR: Please provide 3 valid parameters.
            \rFor Example,
            \r$: ./webscraper.py {Domain} {URL} {Depth} \n
            \r    where Domain can be www.rit.edu
            \r    where URL can be www.rit.edu
            \r    where Depth can be 2
            """)
            if not validParamNum:
                print("\rPlease provide valid number of parameters!")
            if not validDomain:
                print("\rPlease provide a valid Domain!")
            if not validURL:
                print("\rPlease provide a valid URL!")
            if not validDepth:
                print("\rPlease provide a valid Depth number!")
            sys.exit()
        else:
            print("All valid parameters!")
    else:
        print("""
        \rERROR: Please provide 3 valid parameters.
        \rFor Example,
        \r$: ./webscraper.py {Domain} {URL} {Depth} \n
        \r    where Domain can be www.rit.edu
        \r    where URL can be www.rit.edu
        \r    where Depth can be 2
        """)
        sys.exit()

def getDepth():
    if isDepthZero:
        return 0
    else:
        global linkDepth
        depthKeys = list(linkDepth.keys())
        if len(depthKeys) >= 1:
            nowDepth = depthKeys[-1] + 1
            print(nowDepth)
            return nowDepth

def get_request(url, domain):
    if not re.search(domain, url):
        url = 'http://' + domain + url
    elif not re.search('http', url):
        url = 'http://' + url
    return req.get(url).text # HTTP GET

def noDuplicate(linkString, linkDepth):
    keyList = list(linkDepth.keys())
    if len(linkString) != 0:
        for key in linkDepth:
            if linkString in linkDepth.get(key):
                return True
    else:
        return False

def cssResponseParser(linkString):
    matches = re.findall(urlRegexRule,linkString)
    return matches

def jsResponseParser(linkString):
    matches = re.findall(urlRegexRule,linkString)
    return matches

def addToLinkDict(linkString, currDepth, linkDepth):
    if not currDepth in linkDepth:
        if noDuplicate(linkString,linkDepth):
            return False
        else:
            linkDepth[currDepth] = {linkString}
    elif currDepth in linkDepth:
        if noDuplicate(linkString,linkDepth):
            return False
        else:
            linkDepth.get(currDepth).add(linkString)

def responseParser(url, domain):
    httpResponse = get_request(url, domain)
    tree = bs(httpResponse, 'html.parser')

    currDepth = getDepth()
    global linkDepth
    global isDepthZero

    for link in tree.find_all('a'):
        linkString = link.get('href')
        if linkString != None:
            if re.search(domain, linkString):
                if not addToLinkDict(linkString,currDepth,linkDepth):
                    continue
                
    for cssLink in tree.find_all('link'):
        linkString = cssLink.get('href')
        if linkString != None:
            if re.search('.css',linkString) or re.search(domain, linkString):
                cssResponse = get_request(linkString,domain)
                urlInCss = cssResponseParser(cssResponse)
                for list1 in urlInCss:
                    if list1 != None:
                        if re.search(domain, list1):
                           if not addToLinkDict(list1,currDepth,linkDepth):
                                continue 
                

    for jsLink in tree.find_all('script'):
        linkString = jsLink.get('src')
        if linkString != None:
            if re.search('.js', linkString):
                jsResponse = get_request(linkString,domain)
                urlInCss = jsResponseParser(jsResponse)
                for list1 in urlInCss:
                    if list1 != None:
                        if re.search(domain, list1):
                           if not addToLinkDict(list1,currDepth,linkDepth):
                                continue 

    isDepthZero = False        
    return

def parserResponseToFile(linkDict):
    with open("./webscaper_response.txt", "w") as f:
        for key in linkDict:
            urlSet = linkDict.get(key)
            for url in urlSet:
                f.write(url)
        
def main():
    paramVlaue = sys.argv[1:]
    check_parameters(paramVlaue)

    domain = paramVlaue[0]
    url = paramVlaue[1]
    depth = paramVlaue[2]
    
    responseParser(url,domain)
    global linkDepth
    os.system('touch ./webscraper_response.txt')
    os.system('chmod 777 ./webscraper_response.txt')

    parserResponseToFile(linkDepth)

    return

if __name__ == "__main__":
    main()