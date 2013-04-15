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
    
#the following finds all sentences rather than trying to pick out only sentences with the word
def sentences(params):
    w = params['word']
    t = params['text']

    sentenceFind = re.compile('([A-Z][^\.?!]*[\.?!])')
    found = re.findall(sentenceFind,t)
    
    print found
    return found


#testing:
txt = openText("emperor.txt")
p = {'word': "old", 'text': txt}

find(p)

#print txt
