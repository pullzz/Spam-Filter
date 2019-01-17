import cPickle as c 
import os
from collections import Counter
import sys

text = sys.argv[1]

def load(clf_file):
	with open(clf_file) as fp:
		clf = c.load(fp)
	return clf


def make_dict():
	direc = "mails/"
	files = os.listdir(direc)

	emails = [direc + email for email in files]


	words = []
	c = len(emails)

	for email in emails:
		f = open(email)
		blob = f.read()
		words += blob.split(" ")
		#print c
		c -= 1

	for i in range(len(words)):
		if not words[i].isalpha():
			words[i] = ""

	dictionary = Counter(words)
	del dictionary[""]
	return dictionary.most_common(100)


clf = load("text-classifier.mdl")
d = make_dict()
features = []
#inp = raw_input(">")

for word in d:
	features.append(text.count(word[0]))

result = clf.predict([features])
if result[0] == 0:
	print "Not Spam!"
else:
	print "Spam!"

sys.stdout.flush()