# -*- coding: utf-8 -*-
"""
Created on Sun May 31 16:01:01 2020

@author: saksh
"""
from socket import *

def createServer():
    serversocket = socket(AF_INET, SOCK_STREAM)
    try :
        serversocket.bind(("",9000))
        serversocket.listen(5)
        while(1):
            (clientsocket, address) = serversocket.accept()

            rd = clientsocket.recv(5000).decode()
            pieces = rd.split("\n")
            if ( len(pieces) > 0 ) : print(pieces[0])
            """data = "HTTP/1.1 200 OK\r\n"
            data += "Content-Type: text/html; charset=utf-8\r\n"
            data += "\r\n"
            data += "<html><body>Hello World</body></html>\r\n\r\n"
            print(data)
            clientsocket.sendall(data.encode())"""
           
            for word in pieces[0].split():
              if word == "/cdc.txt":
                    f= open("cdc.txt","r")
                    contents=f.read()
                #  print(contents)
                    clientsocket.sendall(contents.encode())
              else:
                  if word == "/": 
                   f= open("textfile.txt","r")
                   contents=f.read()
            #print(contents)
                   clientsocket.sendall(contents.encode())
                  
                  else:
                      if word=='/stop':
                       clientsocket.shutdown(SHUT_WR)

    except KeyboardInterrupt :
        print("\nShutting down...\n");
    except Exception as exc :
        print("Error:\n");
        print(exc)

    serversocket.close()

print('Access http://localhost:9000')
createServer()
