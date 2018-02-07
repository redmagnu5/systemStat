#sysStat
========

#This project contains two scripts, one for server and client. The client script establishes a connection with the server and compiles statistics from the client's host machine, and the sends it to the server for analysis. 
The server script accepts what is sent from the client and stores the information in a sql database. Depending on the paramaters of the sent information, the server will send an email via smtp to the client's email address. 
Lastly, the all the configurations used for the set up of the server and clients information is pulled from an xml file.


Extra notes
--------

- The server script email alert configuration is only configured for 2 clients at the moment.
- The server only stays open till all functions are called. Thus the client script must be executed several times
for the server to fully execute. In the future I would like the server socket to remain open while the rest of the script
runs, as currently you must run the client 4 times for the email alert and database storage functions to run.


Contribute
----------

- Source Code: github.com/redmagnu5/systemStat

Support
-------

As this project was done mainly on a whim, if you have any recommendations or additional input please reach me at epappion117@gmail.com, conscructive 
criticism is always appreciated. 

