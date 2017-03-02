import os
import time;
from markovbot import MarkovBot

# Initialise a MarkovBot instance
tweetbot = MarkovBot()

# Get the current directory's path
dirname = os.path.dirname(os.path.abspath(__file__))
# Construct the path to the book
book = os.path.join(dirname, 'Freud_Dream_Psychology.txt')
# Make your bot read the book!
tweetbot.read(book)

my_first_text = tweetbot.generate_text(25, seedword=['dream', 'psychoanalysis'])
print("tweetbot says:")
print(my_first_text)

# ALL YOUR SECRET STUFF!
# Consumer Key (API Key)
cons_key = 'hETlfJv32tJDRZAy56gRlsyNM'
# Consumer Secret (API Secret)
cons_secret = '0b3ZAADUSfCd5SEHzw5STlvLWyhRV7oWx0qSkbBRs1xa3Jw3at'
# Access Token
access_token = '836076464797708288-PFGXutxkzrsZ2m1xcec6pIfZv4gyDc5'
# Access Token Secret
access_token_secret = 'YzEHE8FfkNLbbzfu8dj2Rpl1lSJRW5R0z8xVdHRbD2f4U'

# Log in to Twitter
tweetbot.twitter_login(cons_key, cons_secret, access_token, access_token_secret)

tweetbot.twitter_tweeting_start(days=0, hours=0, minutes=1, keywords=None, prefix=None, suffix=None)

#tweetbot.twitter_tweeting_stop()

time.sleep(86400)