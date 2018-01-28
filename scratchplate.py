from sklearn.feature_extraction.text import CountVectorizer

s = ["The good boy","The good toy","Already Boon Cursed"]
y = ["The bad boy","The The bad roy"]
vectorizer = CountVectorizer()
train = vectorizer.fit_transform(s)
test = vectorizer.transform(y)
print(vectorizer.get_feature_names()[:10],"\n\n",train,"\n\n",test)
