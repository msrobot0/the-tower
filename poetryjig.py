#!/usr/bin/env python

import nltk


class PoetryJig:

	def __init__(self, filename='v2.txt'):
		f = open("v2.txt","r")
		self.contents = contents =f.read()
		self.lower_contents = contents.lower()
		f.close()
		tokens = nltk.word_tokenize(self.lower_contents)
		print(len(tokens))
		self.lower_text = nltk.Text(tokens)

	def mostcommon(self, count=50):
		dist =nltk.FreqDist(self.lower_text)
		return dist.most_common(count)

	def leastcommon(self, count=50):
		dist =nltk.FreqDist(self.lower_text)
		return dist.most_common()[-count:]
	
	def plot(self):
		dist =nltk.FreqDist(self.lower_text)
		dist.plot()

	def analysis(self):
		dist =nltk.FreqDist(self.lower_text)
		common = dist.most_common()
		return len(common)

	def dist(self, d=50):
		dist =nltk.FreqDist(self.lower_text)
		common =  dict(dist.most_common())
		for word in list(common.keys()):
			if common[word] != d:
				del common[word]
		return common

if __name__ == "__main__":
    jig = PoetryJig()  
    #print(jig.mostcommon())
    #print(jig.leastcommon(5000))
    #dist1 = jig.dist(1)
    #print(dist1)
    #print(len(dist1))
    print(jig.analysis())
    #jig.plot()
