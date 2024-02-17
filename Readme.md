# Advanced KeyLogger in python

Disclaimer: This program has been written for educational purposes only and must not be used for malicious purposes. 

This code is a keylogger coded in python. It is divided into two parts. A client and a server. 

The client runs on the machine whose keystrokes are to be recorded. It will read everything typed on the keyboard and put it in a buffer which will be sent to a remote server after a period of time X (to be defined). 

The server is a multi-client server. For each client, it creates a file with its IP address and records everything received via sockets in this file it has created. 

No sorting is carried out among the data entered by the user. The point of this is to be able to use this data in programs using AI to study user behavior.  
