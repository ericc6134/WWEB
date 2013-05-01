import string
import csv
from collections import Counter
from time import time
import nltk

s = open("texts/lm.txt", "r").read().split(".")
s.extend(open("texts/ash.txt", "r").read().split("."))
s.extend(open("texts/f.txt", "r").read().split("."))
s.extend(open("texts/p-p.txt", "r").read().split("."))
s.extend(open("texts/ts.txt", "r").read().split("."))

s = [ a.translate(string.maketrans("",""), string.punctuation).strip().lower() for a in s if a != '']
while "" in s:
    s.remove("")
start = time()
s = [ nltk.pos_tag(nltk.word_tokenize(w)) for w in s ]
s = [ zip(*x) for x in s ]
print time()-start; start=time()


words = [ x[0] for x in s ]
words = [ w for sent in words for w in sent ]
poses = [ x[1] for x in s ] #part_of_speechs
poses = [ pos for sent in poses for pos in sent ]


toDelete = []
for i in range(len(poses)):
    if poses[i] not in ["JJ","JJR","JJS","NN","NNS","RB","RBR","RBS","VB","VBD","VBG","VBZ"]:
#adjectives, nouns, adverbs, verbs
        toDelete.append(i)

toDelete.reverse()
for i in toDelete:
    del words[i]
    del poses[i]
print len(words) - len(poses)
to_Translate = zip(words,poses) #for testing purposes


with open("poses.csv", "wb") as file:
    fileWriter = csv.writer(file, delimiter="\n", dialect="excel")
    fileWriter.writerow(to_Translate)
with open("words.csv", "wb") as file:
    fileWriter = csv.writer(file, delimiter="\n", dialect="excel")
    fileWriter.writerow(words)
#REMOVE DUPLICATES LATER
