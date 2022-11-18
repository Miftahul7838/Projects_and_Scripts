#!/usr/bin/env python
"""
Name: Miftahul Huq
Date: 09/11/2022
Course: CSEC 380 (Prin Of Web App Sec)
Instructor: Rob Olson
"""

import socket
import time

#sets the neccesary constant variables
SERVER = "hw2.csec380.fun"
PORT = 380
USERAGENT = "CSEC-380"
USERNAME = "alice"
PASSWORD = "SecretPassword123!"
SESSION = None
APIKEY = None
CRLF = "\r\n"

def calibrate():
    """Sends a HTTP request and prints out the HTTP response from the web server"""
    #client connects with the web server
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect((SERVER, PORT))
    #variables of strings used for building HTTP request
    firstline = "POST /jsonLogin HTTP/1.1" + CRLF
    useragentH = "User-Agent:" + USERAGENT + CRLF
    contType = "Content-Type:application/x-www-form-urlencoded" + CRLF
    conLen = len(USERNAME) + len(PASSWORD) + 19
    contLenH = "Content-Length:" + str(conLen) + CRLF
    #HTTP request string
    request = firstline + useragentH + contType + contLenH + CRLF
    request += "username="+ USERNAME +"&password="+ PASSWORD + CRLF
    #client sends HTTP request and recives HTTP response
    client.send(request.encode())
    httpresponse = client.recv(8192)
    response = httpresponse.decode()
    httpresponse = client.recv(8192)
    response = response + httpresponse.decode()
    client.close()
    #stores session key
    global SESSION, APIKEY
    SESSION = response.split('\n')[5].split(' ')[1][:-1] # extracts out the seesion cookie
    APIKEY = response.split('\n')[-1].split(',')[1].split(":")[1][1:-2]

def calibrateSecure():
    """Sends a HTTP request and prints out the HTTP response from the secure site of the web server"""
    global SESSION, APIKEY
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect((SERVER, PORT))
    #proceeds to secure page
    firstline = "POST /jsonSecurePage HTTP/1.1" + CRLF
    useragentH = "User-Agent:" + USERAGENT + CRLF
    sessionCookieH = "Cookie:" + SESSION + CRLF
    contType = "Content-Type:application/x-www-form-urlencoded" + CRLF
    contLenH = "Content-Length:" + str(len(APIKEY) + 7) + CRLF
    #HTTP request stringS
    request = firstline + useragentH + sessionCookieH + contType + contLenH + CRLF
    request += "apikey=" + APIKEY + CRLF
    #client sends HTTP request and recives HTTP response
    client.send(request.encode())
    httpresponse = client.recv(8192)
    response = httpresponse.decode()
    httpresponse = client.recv(8192)
    response = response + httpresponse.decode()
    #closes the connection and prints out the HTTP response
    client.close()
    print(response)

def main():
    calibrate() #calls the function to communicate with the HTTP web server
    calibrateSecure() #calls the fucntions to communicat with secure page of HTTP web server

if __name__ == "__main__":
    main()

