import string
from collections import Counter
from time import time
import nltk

start = time()
s = open("texts/lm.txt", "r").read().split(".")
s = [ a.translate(string.maketrans("",""), string.punctuation).strip().lower() for a in s if a != '']
print s[301]
print nltk.pos_tag(s[300])
#print s
#words = [ a.split(" ") for a in s ]
words = [ w for s in words for w in s if w != "" ]
#words = [ a.split(" ") for a in s ]
#words = [ w for s in words for w in s ]

def createWordList():
    return Counter(words)

#ct =  createWordList()
#print time() - start
#print [ str(i)+": "+str(ct[i]) for i in ct if ct[i] > 500 ]

#ct =  createWordList()
#print type(ct)
print time() - start

