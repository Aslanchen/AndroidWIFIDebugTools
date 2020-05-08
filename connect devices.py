#!/usr/bin/env python3
# -*- coding:UTF-8 -*-

import os
import time
import subprocess
import re
import random

def printDoc():
    print("---------------------Aslan（122560007@163.com）-------------------")
    print("1.Please set adb system environment variable first.")
    print("2.Please connect the phone with USB first.")
    print("3.Please open USB Debug Mode (Setting-> Developer tools-> Debug Mode-> USB debug).")
    print("4.Please connect same WI-FI as the pc.")
    print("---------------------Aslan（122560007@163.com）-------------------")

def connectDevices():
    ret=subprocess.run(["adb", "devices","-l"],stdout=subprocess.PIPE,encoding="utf-8",timeout=8)
    lines=ret.stdout.split('\n')
    for line in lines:
        if line==None or len(line)<=0 or line.startswith("List"):
            continue
        
        matchObj=re.match(r'(\w+)\s*device\s*.+model:(\S*)',line)
        if matchObj==None:
            continue

        if len(matchObj.groups())<2:
            continue

        deviceId=matchObj[1]
        deviceModel=matchObj[2]
        ret=subprocess.run(["adb","-s",deviceId,"shell","ip","-f","inet","addr","show","wlan0"],stdout=subprocess.PIPE,encoding="utf-8",timeout=8)
        ipinfos=ret.stdout.split('\n')
        if ipinfos==None or len(ipinfos)<1:
            continue

        ipinfo=ipinfos[1]
        matchObjIp=re.search(r'(\d+\.?){4}',ipinfo)
        if matchObjIp==None:
            continue

        ipAddress=matchObjIp.group()
        tcpPort=random.randint(1000,9999) 
        os.system("adb -s %s tcpip %s"%(deviceId,tcpPort))
        os.system("adb -s %s connect %s:%s"%(deviceId,ipAddress,tcpPort))
        print("connected to device ",ipAddress,tcpPort,deviceModel)

printDoc()
key=input("Press any to continue...")
connectDevices()

time.sleep(5)