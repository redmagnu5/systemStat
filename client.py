# Create socket and connect
import socket             
s = socket.socket()         
s.connect(('127.0.0.1', 22))
 
#receive data from the server
print s.recv(1024)

# get system information
import win32api
userName = win32api.GetUserName()
sysInfo = win32api.GetSystemInfo()

#Retrieve memory usage %
memStat = win32api.GlobalMemoryStatus()
memUsage = memStat['MemoryLoad']

#retrieve system-wide CPU utilization as %
import psutil
cpuUsage = psutil.cpu_percent(interval=1)

#retrieve system up time (YYYY-MM-DD hr:min:secs)
import datetime
sysUptime = datetime.datetime.fromtimestamp(psutil.boot_time()).strftime("%Y-%m-%d %H:%M:%S")

#retrieve client ip
clientIp = socket.gethostbyname(socket.gethostname())

#Compile all system stats in a list, serialize it to send over socket
import json
stat = [memUsage, cpuUsage, sysUptime, userName, clientIp]
sysStat = json.dumps(stat)

print sysStat

#send all stats over socket
s.send(sysStat)
print s.recv(1024)

