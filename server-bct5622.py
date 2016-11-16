from socket import *
import time
import os.path

servername = 'localhost'
serverPort = 13000

serverSocket = socket(AF_INET, SOCK_STREAM)
serverSocket.bind(('', serverPort))
serverSocket.listen(1)

def parse_message(input):
	words = input.split()
	print(words)
	filename = words[1]
	f = open(filename.replace("/",""), 'r')
	header = "HTTP/1.1 200 OK\r\n\r\n"

	for line in f:
		header = header + line + "\n"
	return header.encode()


while 1:
	connectionSocket, addr = serverSocket.accept()
	sentence = connectionSocket.recv(2048)
	txtSentence = sentence.decode()

	#call function to evaluate the sentence?
	response = parse_message(txtSentence)

	#print('This came from the client:' + txtSentence)
	connectionSocket.send(response)
	connectionSocket.close()