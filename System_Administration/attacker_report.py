#!/usr/bin/env python3

"""
NSSA221 System Administration I: Script_04
Name: Miftahul Huq
Date: 11/02/2021
"""

import os
from geoip import geolite2
from datetime import date
import csv
import re

ip_set = set()
ip_dict = dict()
ip_country = dict()

def myFunc(e):
    """
    This function dictates which the order
    or the attacker IP address
    
    e: the ipaddress
    returns: the number failed login from the IP address
    """
    global ip_dict
    return ip_dict.get(e)

def print_attackers(ip_list):
    """
    prints the report in a organized formated string

    ip_list: a sorted list of all the IP address login fail >= 10
    return: None
    """
    today = date.today()
    d = today.strftime("%b %d, %Y")
    print(f"Attacker Report - {d}\n")
    print(f"# of attackers >= 10 attempts is: {len(ip_list)}\n")
    print("COUNT      IP ADDRESS      COUNTRY")
    for ip in ip_list:
        count = ip_dict.get(ip)
        country = ip_country.get(ip)
        print(f"{count}      {ip}      {country}")
    
    print()

def findIPCountry(ip_list):
    """
    Finds the country of origin of IP address

    ip_list: list of all the IP address with the failed
             login attempts
    return: None
    """
    global ip_country
    global ip_dict
    for ip in ip_list:
        if ip_dict.get(ip) >= 10:
            match = geolite2.lookup(ip)
            if match is not None:
                ip_country[ip] = match.country

def storeIP(ipAddress):
    """
    Checks if the IP is already in the set or not
    and then adds it to the dictionary along with its
    # of failed attemts so far.

    ipaddress: the IP address the failled to log in
    return: None
    """
    global ip_set
    global ip_dict
    
    while True:
        if ipAddress in ip_set:
            ip_list = list(ip_dict.keys())
            try:
                indexOfIP = ip_list.index(ipAddress)
                ip_dict[ipAddress] += 1
                break
            except:
                ip_dict[ipAddress] = 1
                break
        else:
            ip_set.add(ipAddress)

def failedLoginAttempts(logFilename):
    """
    Reads the system log file and tries to figure
    the IP address with the fialed login attempts
    and stores it in the ip_set and ip_dict.

    logFilename: the system log
    return: None
    """
    global ip_dict
    pattern = re.compile(r'(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})')
    with open(logFilename) as file:
        csv_reader = csv.reader(file)
        for line in csv_reader:
            failed_list = re.search('Failed', line[0])
            if (failed_list != None):
                ipaddress = pattern.search(line[0])[0]
                storeIP(ipaddress)

    ip_list = list(ip_dict.keys())
    findIPCountry(ip_list)
    sortedIPAddr = list(ip_country.keys())
    sortedIPAddr.sort(key=myFunc)

    return sortedIPAddr

def main():
    os.system("clear") # clear the screen

    ip_list = failedLoginAttempts("./syslog.log") # returns a list of ip of all the attackers

    print_attackers(ip_list) # prints out current date and the attackers in a organized fassion

if __name__ == '__main__':
    main()