import tweepy
#from time import sleep
import time
import markovify
import random

#Get the bot to read the file
with open("MarkovMod.txt") as f:
	text = f.read()

#building the model
test_model = markovify.NewlineText(text)
#Generate the line of Text
#temp = (test_model.make_sentence(tries=100))
#print("Temp: " + temp)
#List of Starters
listOfStart = ["Breaking News,", "Live Today,", "Reporting Today,"]
starters = random.choice(listOfStart)
#print("Starters: " + starters)
#List Of Atheletes
listOfAth = []
with open('names.txt','r') as f:
	listOfAth = [line.strip() for line in f]

#Could replace text with a children's book
with open("MarkovListFillers.txt") as t:
	abc = t.read()

test2_model = markovify.NewlineText(abc)
#trial = test2_model.make_sentence(tries=100)
model_combo = markovify.combine([test_model, test2_model],[1,1])
temp = model_combo.make_short_sentence(500)
#final = model_combo.make_short_sentence(500)
#print(test2_model)

name = random.choice(listOfAth)
#print("Name: " + name)
#The Secret Stuff
CONSUMER_KEY='UgFKLuORlSybd1cd4ozf4PgHe'
CONSUMER_SECRET='Lsp0HymDxOQPaoAm7vsdQMrgKwrLyYlBNMWOiueZd1ZquzWGhH'
ACCESS_KEY='837052692551782400-s4N8bYZRn4kao6TUCwuN2x3eHoEeCtU'
ACCESS_SECRET='8l2RqUe4ZY4NTuQIqAnvCVUYJVUSJQMyIgWMr3C7QHvSX'

#Update to Twitter
auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
api = tweepy.API(auth)

final = starters + " " + name + " " + temp

#print("Final: "  + final)
#while 1:
print(final)
	#time.sleep(10)
#line = "Testing 123"

#api.update_status(temp)
	#time.sleep(100)