##People parser

def getPeople(filename = "./people.csv"):
	fileHandle = open(filename,"r")
	lines = fileHandle.readlines()
	fileHandle.close()
	people = []

	for line in lines:
		splitLine = line.replace("\n","").split(",")
		if len(splitLine) >= 3:
			dictionary = {"type":splitLine[0].lower(), "email":splitLine[1], "name":splitLine[2]}
			people.append(dictionary)
		else:
			print("Could not understand " + line)

	return people

def writePeople(people, filename = "./people.csv"):
	outputList = []

	for person in people:
		outputList.append(",".join([person["type"], person["email"], person["name"]]))

	outputStr = "\n".join(outputList)
	fileHandle = open(filename, "w")
	fileHandle.write(outputStr)
	fileHandle.close()

if __name__ == "__main__":
	people = getPeople()
	writePeople(people)
	print(people)