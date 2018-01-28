import tweepy 
from textblob import TextBlob 
import csv
import nltk
import py1
import inputdata 
from twitterdata import *
import filetokenize
from sklearn import tree
from sklearn.cross_validation import train_test_split
import scipy
from sklearn.metrics import accuracy_score
from sklearn.neural_network import MLPClassifier	# Classifier #3
import os
import sys
from six.moves import cPickle as pickle 
import googlesearch	
import twittersearch
# Setting up the API

def run(sr,mode):
	Vectorfile,vec = filetokenize.getFileVector("fake_or_real_news.csv")
	Y = filetokenize.getlabels("fake_or_real_news.csv")
	for i in range(len(Y)):
		if Y[i]=="REAL":
			Y[i]="0"
		else:
			Y[i]="1"

	X_train, X_test, Y_train, Y_test = train_test_split(Vectorfile, Y, test_size=1500, random_state=42)


	force = False
	classifier = MLPClassifier(alpha=0.1)
	set_filename = 'model.pickle'
	if os.path.exists(set_filename) and not force:
	  # You may override by setting force=True.
	  print('%s already present - Skipping pickling.' %set_filename)
	else:
		classifier.fit(X_train,Y_train)
		prediction = classifier.predict(X_test)
		accscore = accuracy_score(Y_test,prediction)
		print(accscore)
		data_root = '.'
		pickle_file = os.path.join(data_root, 'model.pickle')
		try:
			f = open(pickle_file, 'wb')
			save = classifier
			pickle.dump(save, f, pickle.HIGHEST_PROTOCOL)
			f.close()
		except Exception as e:
			print('Unable to save data to', pickle_file, ':', e)
			raise
		statinfo = os.stat(pickle_file)
		print('Compressed pickle size:', statinfo.st_size)

	with open('model.pickle','rb') as f:
		classifier = pickle.load(f)

	if mode==0:
		L = []
		L.append(sr)
		RunX = filetokenize.fitnewtoken(L,vec)
		RunY = classifier.predict(RunX)
		if RunY[0]=="0":
			print("According to Database : REAL news")
		else:
			print("According to Database : FAKE news")
		
		twittersearch.returnsentiment(sr)
	else:
		import matplotlib.pyplot as plt
		import matplotlib
		matplotlib.style.use('ggplot')
		twittersearch.getgraphics(sr)
		L = twittersearch.returntweets(sr)
		RunX = filetokenize.fitnewtoken(L,vec)
		RunY = classifier.predict(RunX)
		f=0
		r=0
		for i in RunY:
			if i=='0':
				f+=1
			else:
				r+=1
		fig, ax = plt.subplots()
		plt.bar(x=[10,20],height=[f,r])
		plt.title("Bar Chart of Last 1000 examples in Twitter History")
		plt.xlabel("Type of news Detected(FAKE/REAL)")
		plt.ylabel("Examples encountered")
		plt.show()
