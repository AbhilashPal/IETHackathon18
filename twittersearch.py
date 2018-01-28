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
def getgraphics(sr):
	import matplotlib.pyplot as plt
	import matplotlib
	matplotlib.style.use('ggplot')
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
	#plotting data
	fig, ax = plt.subplots()
	plt.bar(x=[10,20,30],height=[p,nl,ng])
	plt.title("Bar Chart of Last 1000 examples in Twitter History")
	plt.xlabel("Type of Sentiments(Positive/Neutral/Negative)")
	plt.ylabel("Examples encountered")
	plt.show()

	plt.show()
def returntweets(sr):
	auth = tweepy.OAuthHandler(consumer_key,consumer_secret)
	auth.set_access_token(access_token,access_token_secret)
	L=[]
	api = tweepy.API(auth)
	public_tweets = api.search(sr, count=100)
	for tweet in public_tweets:
		L.append(tweet.text)

	return(L)
