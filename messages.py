#Message parser.
#
import random

def readMessages(filename = "./messages.txt"):
	fileHandle = open(filename, "r")
	lines = fileHandle.readlines()
	fileHandle.close()
	outputLines = []
	for line in lines:
		outputLines.append( line.replace("\n","").replace("\\n","\n") )
	return outputLines

def mergeMessage(message, dictionary):
	for k in dictionary.keys():
		if "{"+k+"}" in message:
			message = message.replace("{"+k+"}", dictionary[k])
	return message

def getMessage(dictionary):
	messages = readMessages()
	m = messages[random.randint(0,len(messages)-1)];
	return mergeMessage(m,dictionary)

if __name__ == "__main__":
	dictionary = {"name":"testMan"}
	for message in readMessages():
		print(message)
		print(mergeMessage(message,dictionary))
	print("\n\nPrinting random messages:\n")
	for i in range(10):
		print(getMessage(dictionary))
