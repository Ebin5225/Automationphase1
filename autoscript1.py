'''
Program to automate the Application health check.
This includes reading the log files and checking for the keywords and timestamps to see if the services are up and running.
Also the code checks if the website url is accessible or not
'''

#Modules
import os
import psutil
import datetime
import socket
import getpass
import time
import subprocess
import http.client
from urllib.request import Request, urlopen
from urllib.error import URLError, HTTPError

#Variables
path1="c:/Users/Ebin/Desktop/automation1"
path2="a:/automation2"
path3="d:/automation3"
tm=time.strftime("%d%m%Y")
file1='autosample1.txt'
file2='autosample2.txt'
file3='autosample3.txt'

#Read the log files

def read_logfile1():
    os.chdir(path1)
    loc=os.getcwd()
    status1=False
    #print("Location of Logfile is :",loc)
    with open(file1) as f1:
        for item in f1:
            if str(tm) in item:
                status1=True
                print("Log1 Looks Good, Latest Time stamp is :",item)
                return status1
    if status1==False:
        print("CHECK Log1 Does not contain latest timestamp")
            
def read_logfile2():
        os.chdir(path2)
        loc=os.getcwd()
        status2=False
        #print("Location of Logfile is :",loc)
        with open (file2) as f2:
            for item in f2:
                if str(tm) in item:
                    status2 =True
                    print("Log2 Looks Good, Latest Time stamp is :",item)
                    return status2
        if status2==False:
                print("CHECK Log2 Does not contain latest timestamp")
                
def read_logfile3():
    os.chdir(path3)
    loc=os.getcwd()
    status3=False
    #print("Location of Logfile is :",loc)
    with open (file3) as f3:
        for item in f3:
            if str(tm) in item:
                status3=True
                print("Log3 Looks Good, Latest Time stamp is :",item)
                return status3
    if status3==False:
        print("CHECK Log3 Does not contain latest timestamp")

#Function to check the status of website
def website_health_check():
    req = Request("http://google.com")
    try:
        response = urlopen(req)
    except HTTPError as e:
        print('The server couldn\'t fulfill the request.')
        print('Error code: ', e.code)
    except URLError as e:
        print('We failed to reach a server.')
        print('Reason: ', e.reason)
    else:
        print ('Website is working fine')

 #Main function defenition           
def main_function():
    print('*'*50,'\n')
    read_logfile1()
    print('*'*50,'\n')
    read_logfile2()
    print('*'*50,'\n')
    read_logfile3()
    print('*'*50,'\n')
    website_health_check()
    print('*'*50,'\n')

#Ignition key
main_function()

    
    
