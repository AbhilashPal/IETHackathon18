import nltk
import csv
import pandas as pd

from sklearn.feature_extraction.text import CountVectorizer
import csv

def getlabels(x):

	k = []
	data = pd.read_csv(x, usecols = [3])
	text = []
	for i in range(int(len(data))):
		text.append(data['label'][i])
	return text



def getbagofwords(t):
	for i in t:
		i = str(i)
	vectorizer = CountVectorizer()
	bagofwords = vectorizer.fit(t)
	bagofwords = vectorizer.transform(t)
	return bagofwords,vectorizer

def getFileVector(x):

	k = []
	data = pd.read_csv(x, usecols = [2])
	text = []
	for i in range(int(len(data))):
		text.append(data['text'][i])
	
	#now tokenizing
	vector = getbagofwords(text)
	return vector

def fitnewtoken(n,vectorizer):
	for i in n:
		i=str(i)
	newbagX = vectorizer.transform(n)
	return newbagX