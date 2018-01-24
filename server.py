# -*- coding: utf-8 -*-
"""

@author: redMagnu5
"""



#Retrieves attributes from xml config file 
class Config:
    import xml.etree.cElementTree as ET
    tree = ET.parse('config.xml')
    root = tree.getroot()
    IP = root[0][0].text
    port = int(root[0][1].text)
    email = root[0][2].text
    
    def _init_(self, IP, port, email):
        self.IP = IP
        self.port = port
        self.email = email
 
#Gets client IP address from output of Socket(), checks if received IP address
#matches with any pre-configured IP in xml.config, then assigns the email address
#corresponding to received IP. Royal pain in my a$$.        
def clientEmail():
    import xml.etree.cElementTree as ET
    tree = ET.parse('config.xml')
    root = tree.getroot()
    clientEmail = root[0][2].text
    clientIP = []
    stat = Socket()
    statIP = stat[1]
    for client in root.findall('client'):
        IP = client.find('ip').text
        clientIP.append(IP)
    for i in xrange(1,len(clientIP)):
        if clientIP[i] == statIP:
            if statIP==root[1][1].text:
                clientEmail = root[1][0].text
            if statIP==root[2][1].text:
                clientEmail = root[2][0].text 
    print clientEmail
    return clientEmail
           
#Creates server socket and receives data from client
def Socket(): 
    import socket  
    import json          
    s = socket.socket()         
    print "Socket successfully created"
    s.bind((Config.IP, Config.port))
    print "socket binded to %s" %(Config.port)
    s.listen(5)     
    print "socket is listening"
    c, addr = s.accept()
    print 'Got connection from', addr
    c.send('Thank you for connecting')
    rcv = json.loads(c.recv(10000))
    c.send('Received system stats')
    s.close()
    return rcv

#Send email over smtp when sys stats reach certain threshold
def smtp():
    import smtplib
    stat = Socket()
    server = smtplib.SMTP('smtp.gmail.com:587')
    server.starttls()
    if (stat[2] or stat[3]) >= 50:
        email = clientEmail()
        username = raw_input('Enter username :' )
        password = raw_input('Enter password :' )
        server.login(username,password)
        try:
            server.sendmail(Config.email, [email],'test')
        finally:
            server.quit()
      
#Create a db and store values received from client           
def sql():
    import sqlite3
    conn = sqlite3.connect('sysStat.db')
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS sysStats
                 (User Name, Client IP, Memory Usage, CPU Usage, System Uptime)''')
    stat = Socket()
    c.execute('INSERT INTO sysStats VALUES (?,?,?,?,?)', stat)         
    conn.commit()
    conn.close()

if __name__ == "__main__":
    
    Socket()
    sql()
    smtp()
    clientEmail()
