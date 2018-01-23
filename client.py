# -*- coding: utf-8 -*-
"""

@author: redMagnu5
"""


# Create client socket and connect to server
def Socket():
    import socket
    from server import Config             
    s = socket.socket()         
    s.connect((Config.IP, Config.port))
    print s.recv(10000)
    s.send(sysStat())
    print s.recv(10000)
    return s

#Gathers client system statistics 
def sysStat():    
    import win32api
    import psutil
    import socket
    import datetime
    import json
    userName = win32api.GetUserName()
    memStat = win32api.GlobalMemoryStatus()
    memUsage = memStat['MemoryLoad']
    cpuUsage = psutil.cpu_percent(interval=1)
    clientIp = socket.gethostbyname(socket.gethostname())
    sysUptime = datetime.datetime.fromtimestamp(psutil.boot_time()).strftime("%Y-%m-%d %H:%M:%S")
    stat = [userName, clientIp, memUsage, cpuUsage, sysUptime]
    sysStat = json.dumps(stat)
    return sysStat

    
sysStat()
Socket()

