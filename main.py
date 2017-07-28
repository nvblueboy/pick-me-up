##pick-me-up, a text-based memelord.
# Dylan Bowman 2017
# Version 0.1


#Local imports
import reddit, emailLib, people
#Python imports
import configparser, time, traceback

def main():
	config = configparser.ConfigParser()
	config.read("config.ini")
	admin = config["email"]["admin"]

	try:
		sendTime = time.strptime(config["email"]["send"],"%I:%M %p")
	except:
		print("Couldn't understand your send time. Assuming send time to be now.")
		sendTime = time.localtime()

	lastDaily = 0
	run_app = True

	while(run_app):
		lt = time.localtime()
		if lt[3] == sendTime[3] and lt[4] == sendTime[4] and lastDaily != lt[7]:
			lastDaily = lt[7]
			sendMessages(config)

def send_text(config,to,body):
    user = config["email"]["user"]
    password = config["email"]["password"]
    smtp_addr = config["email"]["smtp_server"]
    emailLib.send_email(user,password,to,"",body,smtp_addr)

def send_attachment(config,to,body,file):
    user = config["email"]["user"]
    password = config["email"]["password"]
    smtp_addr = config["email"]["smtp_server"]
    emailLib.send_attachment(user,password,to,"",body,file,smtp_addr)

def sendMessages(config):
	#Step 1:get top post from reddit.
	p = reddit.sendable(config)
	messageForAll = "Here's a wholesome meme: " + p["title"]

	peopleList = people.getPeople()

	for person in peopleList:
		customMessage = ""


		if p["is_photo"]:
			send_attachment(config,person["email"],customMessage + messageForAll, p["location"])
		else:
			send_text(config,person["email"], customMessage + messageForAll + " @ " + p["url"])
		print("Sent to "+person["name"])

if __name__ == "__main__":
	main()