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
	#change directory
	#dir = os.chdir('/AthletePic/')
	filename = os.path.abspath('AthletePic/Michael Phelps.jpg')

	#print(filename)
	#api.update_status(final)
	#api.update_with_media(filename,final)
	time.sleep(2)

	#time.sleep(100)