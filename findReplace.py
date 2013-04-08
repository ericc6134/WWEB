import re

def openText(txt):
    t = ""
    l = open(txt).readlines()
    for line in l:
        t = t + line

    return t

txt = openText("emporer.txt")

def find(params):
    w = params['word']
    t = params['text']

    sentenceFind = re.compile('[.?!] .*? ' + w + ' .*?[.?!]')
    found = re.findall(sentenceFind,t)
    
    print found
    return found

    #print w + " and " + t

p = {'word': "old", 'text': txt}

find(p)

#print txt
