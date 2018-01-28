import tweepy
from twitterdata import *
from textblob import TextBlob 

def returnsentiment(sr):
	auth = tweepy.OAuthHandler(consumer_key,consumer_secret)
	auth.set_access_token(access_token,access_token_secret)

	api = tweepy.API(auth)
	public_tweets = api.search(sr, count=1000)
	c=0
	p=0
	ng=0
	nl=0
	for tweet in public_tweets:
		c+=1
		analysis = TextBlob(tweet.text)
		if float(analysis.sentiment[0]) > 0:
			p+=1
		elif float(analysis.sentiment[0]) < 0:
			ng+=1
		else:
			nl+=1
	if(p>ng):
		print("Most users are Positive about this issue.")
	else:
		print("Most users are Negative about this issue.")
