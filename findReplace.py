import re

#opens the text file and returns it as one string
def openText(txt):
    t = ""
    l = open(txt).readlines()
    for line in l:
        t = t + line

    return t

#the following finds every sentence with the word in question but gives quite a bit more than you need
#params should have {'word': *word*, 'text' : *text to search*}
#returns a list of the sentences that include *word*
def find(params):
    w = params['word']
    t = params['text']

    sentenceFind = re.compile('[.?!] .*? ' + w + ' .*?[.?!]')
    found = re.findall(sentenceFind,t)
    
    print found
    return found

    #print w + " and " + t

#testing:
txt = openText("emperor.txt")
p = {'word': "old", 'text': txt}

find(p)

#print txt
