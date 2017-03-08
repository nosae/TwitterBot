#Utilizes jsvine Markovify chain models
import tweepy, time, markovify, random, os

#Get the bot to read the file
with open("Freud_Dream_Psychology.txt") as f:
	text = f.read()

#List Of Atheletes
listOfAth = []
with open('names.txt','r') as f:
	listOfAth = [line.strip() for line in f]

#Could replace text with a children's book
with open("MarkovMod.txt") as t:
	abc = t.read()

def getPic(name): 
	f1Name = ""
	if name == "Usain Bolt": 
		f1Name = os.path.abspath('AthletePic/Usain Bolt.jpg')
	elif name == "Michael Jordan":
		f1Name = os.path.abspath('AthletePic/Michael Jordan.jpg')
	elif name == "Kobe Bryant":
		f1Name = os.path.abspath('AthletePic/Kobe Bryant.jpg')
	elif name == "Tiger Woods":
		f1Name = os.path.abspath('AthletePic/Tiger Woods.jpg')
	elif name == "Michael Jordan":
		f1Name = os.path.abspath('AthletePic/Michael Jordan.jpg')
	elif name == "The MIT Blackjack Team":
		f1Name = os.path.abspath('AthletePic/The MIT Blackjack Team.jpg')
	elif name == "Muhammad Ali":
		f1Name = os.path.abspath('AthletePic/Muhammad Ali.jpg')
	elif name == "Shaquille O\'Neal":
		f1Name = os.path.abspath('AthletePic/Shaquille ONeal.jpg')
	elif name == "Stephen Curry":
		f1Name = os.path.abspath('AthletePic/Stephen Curry.jpg')
	elif name == "Kevin Durant":
		f1Name = os.path.abspath('AthletePic/Kevin Durant.jpg')
	elif name == "Lance Armstrong":
		f1Name = os.path.abspath('AthletePic/Lance Armstrong.jpg')
	elif name == "Lionel Messi":
		f1Name = os.path.abspath('AthletePic/Lionel Messi.jpg')
	elif name == "Floyd Mayweather":
		f1Name = os.path.abspath('AthletePic/Floyd Mayweather.jpg')
	elif name == "Michael Phelps":
		f1Name = os.path.abspath('AthletePic/Michael Phelps.jpg')
	elif name == "Peyton Manning":
		f1Name = os.path.abspath('AthletePic/Peyton Manning.jpg')
	elif name == "Serena Williams":
		f1Name = os.path.abspath('AthletePic/Serena Williams.jpg')
	elif name == "Babe Ruth":
		f1Name = os.path.abspath('AthletePic/Babe Ruth.jpg'	)
	elif name == "Mike Tyson":
		f1Name = os.path.abspath('AthletePic/Mike Tyson.jpg')	
	elif name == "Valentia Vezzai":
		f1Name = os.path.abspath('AthletePic/Valentia Vezzai.jpg')
	elif name == "Dan Lin":
		f1Name = os.path.abspath('AthletePic/Dan Lin.jpg')	
	elif name == "Carl Lewis":
		f1Name = os.path.abspath('AthletePic/Carl Lewis.jpg')	
	elif name == "David Douillet":
		f1Name = os.path.abspath('AthletePic/David Douillet.jpg')			
	return f1Name

while 1:
	#building the model
	test_model = markovify.NewlineText(text)
	test2_model = markovify.NewlineText(abc)
	#List of Starters
	listOfStart = ["Breaking News,", "Live Today,", "Reporting Today,", "Hello World,", "Good Afternoon,", "Tonight,"]
	#randomly choose from starting list
	starters = random.choice(listOfStart)
	#combination using markovify
	model_combo = markovify.combine([test_model, test2_model],[1,1])
	temp = test2_model.make_sentence(tries=100)
	#temp = model_combo.make_short_sentence(400,tries=100)
	#final = model_combo.make_short_sentence(500)
	#print(test2_model)

	name = random.choice(listOfAth)

	# The Secret Stuff for TwitBot
	# Consumer Key
	CONSUMER_KEY = 'hETlfJv32tJDRZAy56gRlsyNM'
	# Consumer Secret (API Secret)
	CONSUMER_SECRET = '0b3ZAADUSfCd5SEHzw5STlvLWyhRV7oWx0qSkbBRs1xa3Jw3at'
	# Access Token
	ACCESS_KEY = '836076464797708288-PFGXutxkzrsZ2m1xcec6pIfZv4gyDc5'
	# Access Token Secret
	ACCESS_SECRET = 'YzEHE8FfkNLbbzfu8dj2Rpl1lSJRW5R0z8xVdHRbD2f4U'

	#Update to Twitter
	auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
	auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
	api = tweepy.API(auth)

	final = starters + " " + name + " " + temp

	print(final)
	#Find picture now from list of names
	filename = getPic(name)
	#api.update_status(final)
	api.update_with_media(filename,final)
	time.sleep(100)
