import string

s = open("texts/lm.txt", "r").readlines()
s = [ a.translate(string.maketrans("",""), string.punctuation).strip() for a in s if a != '']
#print s
words = [ a.split(" ") for a in s ]
words = [ w for s in words for w in s ]
#print words
freqs = {}
print freqs["hey"]
def createWordList():
    for w in words:
        if word in freqs.keys():
            freqs[word] = freqs[word] + 1
        else:
            freqs[word] = 1

