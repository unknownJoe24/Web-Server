#import socket module
from fileinput import filename
from socket import *
import sys # In order to terminate the program

serverSocket = socket(AF_INET, SOCK_STREAM)
#Prepare a server socket
serverPort = 8080
serverSocket.bind(('',serverPort))
serverSocket.listen(1)

while True:
    #Establish the connection
    print('Ready to serve...')
    connectionSocket, addr = serverSocket.accept()#Fill in start and end
    try:
        message = connectionSocket.recv(1024)
        #print(message)
        filename = message.split()[1]
        f = open(filename[1:])
        print(f)
        outputdata = f.read()
        f.close()
        #Send one HTTP header line into socket
        #send HTTP header line
        connectionSocket.send('HTTP/1.1 200 OK\r\n'.encode())
        connectionSocket.send("Content-Type: text/html\r\n\r\n".encode())
        
        #Send the content of the requested file to the client
        for i in range(0, len(outputdata)):
            print("sending data")
            connectionSocket.send(outputdata[i].encode())
        connectionSocket.send("\r\n".encode())

        connectionSocket.close()
    except:
        #Send response message for file not found
        #404 error
        print("File not found")
        connectionSocket.send('HTTP/1.1 404 Not Found \r\n'.encode())
        #Close client socket
        connectionSocket.close()
serverSocket.close()
sys.exit() #Terminate the program after sending the corresponding data
