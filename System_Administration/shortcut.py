#!/usr/bin/env python3

"""
NSSA221 System Administration I: Script_01
Name: Miftahul Huq
Date:09/17/2021
"""

import os
import subprocess
import time

LINK_PATH = "/home/student/"

# User command options display.
def cmd_options():
    os.system("clear")
    print("""\n

                ************************************************
                ***************\033[1;32;40m Shortcut Creater \033[0m***************
                ************************************************

    Enter Selection:

            1 - Create a shortcut in your home directory.
            2 - Remove a shortcut from our home directory.
            3 - Run shortcut report.
    \n""")

# finds the orginal file and file can a link file depending on if link = True or False
def findFile(filename, link=False):
    if link:
        cmd = "sudo find / " + filename + " -type l | grep " + filename
    elif link == False:
        cmd = "sudo find " + LINK_PATH + " " + filename + " -type f | grep " + filename
        
    p = subprocess.run(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
    out = p.stdout.decode()
    err = p.stderr.decode()

    filePath = out.split("\n")

    if len(out) == 0:
        return False

    elif len(out) != 0:
        for path in filePath:
            splitPath = path.split("/")
            if splitPath[-1] == filename:
                return path

# creates symbolic link in the /home/student/ directory
def create_shortcut():
    os.system("echo student | sudo --stdin clear")
    filename = input("Please enter the file name to create a shortcut:    ")
    result = findFile(filename)
    if result != False:
        confirm = input("Found " + result + ". Select Y/y to create shortcut.  ")
        print("Creating Shortcut, please wait... ")
        if confirm == 'Y' or confirm == 'y':
            cmd = "sudo ln -s " + result + " " + LINK_PATH
            p = subprocess.run(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
            out = p.stdout.decode()
            err = p.stderr.decode()
            if len(err) != 0:
                print("\nThe shortcut for " + result + " has already been created.")
                print("Returning to Main Menu")
                time.sleep(1)
            elif len(err) == 0:
                print("\nShortcut created. Returning to Main Menu.")
                time.sleep(1)
    else:
        print("\nSorry, couldn't find " + filename + "!")
        print("Returning to Main Menu")
        time.sleep(1)

# removes the symbolic links in /home/student/ directory
def remove_shortcut():
    os.system("echo student | sudo --stdin clear")
    filename = input("Please enter the shortcut/link to remove:    ")
    print("Searching, please wait...")
    result = findFile(filename,True)
    if result != False:
        try:
            os.system("sudo rm " + result)
            print("\nRemoved shortcut " + result + ". Returning to Main Menu.")
            time.sleep(1)
        except:
            print("\nSorry, couldn't find " + filename)
            print("Returning to Main Menu")
            time.sleep(1)
    else:
        print("\nSorry, couldn't find " + filename)
        print("Returning to Main Menu")
        time.sleep(1)

# finds the symbolic links in the /home/student/ directory
def symlink_list():
    symLink_list = []
    cmd = "sudo find " + LINK_PATH + " -type l -ls"
    p = subprocess.run(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
    out = p.stdout.decode()
    result = out.split("\n")
    for link in result:
        filePath = link.split()
        if len(filePath) != 0:
            file = filePath[10].split("/")
            if len(file) == 4:
                symLink_list.append(file[-1])
    
    if len(symLink_list) == 0:
        return False
    
    else:
        return symLink_list

# prints the symbolic links in the /home/student/ directory 
def shortcut_report():
    os.system("echo student | sudo --stdin clear")
    os.system("cd /home/student")
    p = subprocess.run("pwd",stdout=subprocess.PIPE, stderr=subprocess.PIPE,shell=True)
    print("Your current directory is /home/student.")

    linkDict = dict()
    
    result = symlink_list()
    if result != False:
        print("\n\nThe number of links is " + str(len(result)))
        print("\nSymbolic Link                  Target Path")
        for link in result:
            cmd = "sudo readlink -f " + LINK_PATH + link
            target = subprocess.run(cmd,stdout=subprocess.PIPE, stderr=subprocess.PIPE,shell=True)
            print(f"{link}                      {target.stdout.decode()} ")

    else:
        print("\n\nThe number of links is 0")
        print("\nSymbolic Link                  Target Path")

    print("\nTo return to the Main Menu, press Enter. Or select R/r to remove a link.")
    select = input()
    if select == "\n":
        return
    elif select == "R" or select == "r":
        remove_shortcut()
        
                
def main():
    os.system("echo student | sudo --stdin clear")
    while True:
        cmd_options()
        userInput = input('Please enter a number (1-3) or "Q/q" to enter the program.    ')
        if userInput == 'q' or userInput == 'Q' or userInput == "quit" or userInput == "Quit":
            break
        elif userInput == "1":
            create_shortcut()
        elif userInput == "2":
            remove_shortcut()
        elif userInput == "3":
            shortcut_report()
        else:
            print("\n\nPlease a numer between (1-3)...")
            time.sleep(2)


if __name__ == '__main__':
    main()