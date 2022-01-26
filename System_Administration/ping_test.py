#!/usr/bin/env python3

"""
NSSA221 System Administration I: Script_01
Name: Miftahul Huq
Date:09/17/2021
"""

import os
import subprocess
import shlex
import time

# Finds gateway
def find_Gtw(defaultGtw):
    cmd = shlex.split("ip r")
    p1 = subprocess.Popen(cmd, shell=False, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    out, err = p1.communicate()
    defaultGtw = out.decode().split()[2]
    return defaultGtw

# User command options display.
def cmd_options():
    print()
    os.system("clear")
    print("Enter Selection:\n")
    print("       1 - Test connectivity to your gateway")
    print("       2 - Test for remote connectivity")
    print("       3 - Test for DNS resolution")
    print("       4 - Display gateway IP Address")
    print("\n")

# Test connectivity to the gateway
def gtw_connecton(defaultGtw):
    cmd = ["ip","r"]
    os.system("clear")
    print("Testing connectivity to your gateway...")
    time.sleep(1)
    os.system("clear")
    print("Running test, please wait.\n\n")
    p1 = subprocess.Popen(cmd, shell=False, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    out, err = p1.communicate()
    defaultGtw = out.decode().split()[2]
    cmd = shlex.split("ping -c4 " + defaultGtw)
    p2 = subprocess.Popen(cmd, shell=False, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    out, err = p2.communicate()
    pingResult = out.decode().split()
    try:
        verify = pingResult[7] + " " + pingResult[8] + " " + pingResult[9] + " " + pingResult[10]
        if "64 bytes from " + defaultGtw+":" == verify:
            print("Please inform your system administrator that the test was SUCCESSFUL!")
        else:
            print("Please inform your system administrator that the test has FAILED!")
    except:
        print("Please inform your system administrator that the test has FAILED!")
    time.sleep(3)
    
# Test for remote connectivity
def rmt_connectivity():
    remote = "129.21.3.17"
    os.system("clear")
    print("Testing for remote connectivity... trying IP address " + remote)
    time.sleep(1)
    os.system("clear")
    print("Running test, Please wait.\n\n")
    cmd = shlex.split("ping -c4 " + remote)
    p2 = subprocess.Popen(cmd, shell=False, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    out, err = p2.communicate()
    pingResult = out.decode().split()
    try:
        verify = pingResult[7] + " " + pingResult[8] + " " + pingResult[9] + " " + pingResult[10]
        if "64 bytes from " + remote+":" == verify:
            print("Please inform your system administrator that the test was SUCCESSFUL!")
        else:
            print("Please inform your system administrator that the test has FAILED!")
    except:
        print("Please inform your system administrator that the test has FAILED!")
    time.sleep(3)

# # Test for DNS resolution
def dns_resolution():
    remote = "www.google.com"
    os.system("clear")
    print("Resolving DNS: trying URL... " + remote)
    time.sleep(1)
    os.system("clear")
    print("Running test, Please wait.\n\n")
    cmd = shlex.split("ping -c4 " + remote)
    p2 = subprocess.Popen(cmd, shell=False, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    out, err = p2.communicate()
    pingResult = out.decode().split()
    try:
        remote = pingResult[2]
        verify = pingResult[7] + " " + pingResult[8] + " " + pingResult[9] + " " +pingResult[11]
        if "64 bytes from " + remote+":" == verify:
            print("Please inform your system administrator that the test was SUCCESSFUL!")
        else:
            print("Please inform your system administrator that the test has FAILED!")
    except:
        print("Please inform your system administrator that the test has FAILED!")
    time.sleep(3)

# # Display gateway IP Address
def gtw_ip_address(defaultGtw):
    os.system("clear")
    if len(defaultGtw) > 7:
        print("Your gateway IP addres is " + defaultGtw + ".")
    else:
        print("The default gateway is not found or not in the system")
    time.sleep(3)

def main():
    defaultGtw = ""
    userInstruct = "Please enter a \33[1;32;40m number (1-4) \033[0m or \33[1;32;40m \"Q\q\" \033[0m to quit the program.   "
    cmd_options()
    userInput = input(userInstruct)
    while True:
        defaultGtw = find_Gtw(defaultGtw)
        if userInput == 'q' or userInput == 'Q':
            break
        elif userInput == '1':
            gtw_connecton(defaultGtw)
        elif userInput == '2':
            rmt_connectivity()
        elif userInput == '3':
            dns_resolution()
        elif userInput == '4':
            gtw_ip_address(defaultGtw)
        else:
            print("\n\nPlease select a number between 1 through 4.")
            time.sleep(3)
        
        cmd_options()
        userInput = input(userInstruct)
    
    os.system("clear")

if __name__ == '__main__':
    main()