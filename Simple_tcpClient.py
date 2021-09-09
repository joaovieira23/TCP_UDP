from socket import *
serverName = "127.0.0.1"
serverPort = 27123
clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket.connect((serverName,serverPort))
sentence = input("Input lowercase sentence: ")
clientSocket.send(bytes(sentence, "utf-8"))
modifiedSentence = clientSocket.recv(1024)
text = str(modifiedSentence,"utf-8")
print ("Received from Make Upper Case Server: ", text)
clientSocket.close()