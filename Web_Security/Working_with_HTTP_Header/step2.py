#!/usr/bin/env python
"""
Name: Miftahul Huq
Date: 09/11/2022
Course: CSEC 380 (Prin Of Web App Sec)
Instructor: Rob Olson
"""

import socket

#sets the neccesary constant variables
SERVER = "hw2.csec380.fun"
PORT = 380
USERAGENT = "CSEC-380"
USERNAME = "alice"
PASSWORD = "SecretPassword123!"
CRLF = "\r\n"

def calibrate():
    """Sends a HTTP request and prints out the HTTP response from the web server"""
    #client connects with the web server
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect((SERVER, PORT))
    #variables of strings used for building HTTP request
    firstline = "GET /test HTTP/1.1" + CRLF
    secondline = "User-Agent:" + USERAGENT + CRLF
    #HTTP request string
    request = firstline + secondline + CRLF
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

if __name__ == "__main__":
    main()

