##People parser

def getPeople(filename = "./people.csv"):
	fileHandle = open(filename,"r")
	lines = fileHandle.readlines()
	fileHandle.close()
	people = []

	for line in lines:
		splitLine = line.replace("\n","").split(",")
		if len(splitLine) >= 3:
			dictionary = {"type":splitLine[0].lower(), "text":splitLine[1].lower(), "meme":splitLine[2].lower(), "email":splitLine[3], "name":splitLine[4]}
			people.append(dictionary)
		else:
			print("Could not understand " + line)

	return people

def writePeople(people, filename = "./people.csv"):
	outputList = []

	for person in people:
		outputList.append(",".join([person["type"], person["text"], person["meme"], person["email"], person["name"]]))

	outputStr = "\n".join(outputList)
	fileHandle = open(filename, "w")
	fileHandle.write(outputStr)
	fileHandle.close()

if __name__ == "__main__":
	people = getPeople()
	writePeople(people)
	print(people)