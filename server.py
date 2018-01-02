import json
import socket

def Port():
    from xml.dom import minidom
    xmldoc = minidom.parse('config.xml')
    itemList = xmldoc.getElementsByTagName('item')
    port = int(itemList[1].attributes['port'].value)
    return port

def Socket():              
    s = socket.socket()         
    print "Socket successfully created"
    s.bind(('', Port()))
    print "socket binded to %s" %(Port())
    s.listen(5)     
    print "socket is listening"
    
    #maybe define a new function that retrieves data and prints it
    c, addr = s.accept()
    print 'Got connection from', addr
    c.send('Thank you for connecting')
    sysStat = json.loads(c.recv(10000))
    c.send("received your stuff")
    return sysStat
    
            
            
Port()
Socket()
