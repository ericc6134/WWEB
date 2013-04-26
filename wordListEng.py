import string
from collections import Counter
from time import time

s = open("texts/lm.txt", "r").readlines()
s = [ a.translate(string.maketrans("",""), string.punctuation).strip().upper() for a in s if a != '']
#print s
words = [ a.split(" ") for a in s ]
words = [ w for s in words for w in s ]


def createWordList():
    return Counter(words)

start = time()
ct =  createWordList()
print type(ct)
print time() - start
