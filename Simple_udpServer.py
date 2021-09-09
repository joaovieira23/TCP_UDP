from socket import *
serverPort = 12500
serverSocket = socket(AF_INET, SOCK_DGRAM)
serverSocket.bind(("", serverPort))
print ("UDP server\n")
while 1:
    message, clientAddress = serverSocket.recvfrom(2048)
    text = str(message,"utf-8") #cp1252 #utf-8
    print ("Received from Client: ", text)