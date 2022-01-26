#!/usr/bin/env python3

"""
NSSA221 System Administration I: Script_02
Name: Miftahul Huq
Date: 09/27/2021
"""

import os
import shlex
import subprocess
import time
import csv

header_index = []
emp_identical_name = dict()

def read_csv_file(filename):
    """
    A file reader
    filename: the absolute file path or relative filepath
    returns: a 2d list of the content in the file
    """
    firstline = []
    contentDetail = []
    
    try:
        with open(filename) as file:
            isFirstLine = True
            csv_reader = csv.reader(file)
            for line in csv_reader:
                if isFirstLine == True:
                    firstline = line
                    isFirstLine = False
                else:
                    for i in range(len(line)):
                        aString = "".join(char for char in line[i] if char.isalnum()) # goes throug the each work in a line and get rid of special character
                        line[i] = aString

                    contentDetail.append(line)

        for content in contentDetail:
            if len(content) == len(firstline):
                if content[-1] == '':
                    content.pop(-1)
        firstline.pop(-1)
                
    except:
        print("Incorrect file path")
                
    return firstline, contentDetail

def add_user(empID, empName, department, group):
    # Creates the directory that the employee belongs to
    cmd = shlex.split("sudo mkdir /home/" + department)
    p1 = subprocess.Popen(cmd, shell=False, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    out, err = p1.communicate()

    # Creates the group that the employee belongs to
    cmd = shlex.split("sudo groupadd " + group)
    p1 = subprocess.Popen(cmd, shell=False, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    out, err = p1.communicate()

    #creates the user
    while True:
        if group == "office":
            cmd = shlex.split("sudo useradd " + empName + " -g " + group + " -c " + empID + " -d /home/" + department + "/" + empName + " -s /bin/csh")
        else:
            cmd = shlex.split("sudo useradd " + empName + " -g " + group + " -c " + empID + " -d /home/" + department + "/" + empName + " -s /bin/bash")

        p1 = subprocess.Popen(cmd, shell=False, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        out, err = p1.communicate()
        outlist = err.decode().split()
        try:
            if outlist[-1] == "exists":
                try:
                    s = list(empName)
                    s[-1] = str(int(s[-1]) + 1)
                    aString = "".join(s)
                    empName = aString
                    continue
                except:
                    empName += str(1)
                    continue
            else: 
                break
        except:
            break

    # Sets password
    os.system('echo "echo password | passwd --stdin ' + empName + '" | sudo su >/dev/null 2>&1')

    # expres the password
    cmd = shlex.split("sudo passwd -e " + empName)
    p1 = subprocess.Popen(cmd, shell=False, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    out, err = p1.communicate()

    return empName

def add_valid_user(fileContent):
    global header_index

    for content in fileContent:
        if len(content) > len(header_index):
            print("Cannot process employee ID ", content[header_index.index("EmployeeID")], "     Insufficient data.\n")
        elif content[header_index.index("Group")] == "area51":
            print("Cannot process employee ID ", content[header_index.index("EmployeeID")], "     Not a valid group.\n")
        elif content[header_index.index("Department")] == '':
            print("Cannot process employee ID ", content[header_index.index("EmployeeID")], "     Does not belong to any department.\n")
        elif content[header_index.index("EmployeeID")] == '':
            print("Cannot process the employee     Does not have an employee ID.\n")
        else:
            empName = content[header_index.index("FirstName")][0] + content[header_index.index("LastName")]
            empID = content[header_index.index("EmployeeID")]
            department = content[header_index.index("Department")]
            group = content[header_index.index("Group")]
            empName = add_user(empID, empName.lower(), department, group)
            print("Processing employee ID " + empID + "           " + empName + " added to system.\n")

def main():
    global header_index
    os.system("clear")

    print("\nAdding new users to the system.")
    print("Please Note: The default password for new users is password.")
    print("For testing purposes. Change the password to 1$4pizz@.\n")

    filename = "/home/student/scripts/script02/linux_users.csv"

    header_index, content = read_csv_file(filename) 

    add_valid_user(content) # checks the users and validate if they can be added or not and adds it.

if __name__ == '__main__':
    main()