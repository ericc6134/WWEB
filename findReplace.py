import re

#opens the text file and returns it as one string
def openText(txt):
    l = open(txt).readlines()

    return l

def stringify(lst):
    s = ""
    for line in lst:
        s = s + line

    return s

#testing:
txt = stringify(openText("emperor.txt"))
p = {'word': "old", 'text': txt, 'words': ["new","all"]}

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
    
    #print found
    return found

#print "find(p): "
#find(p)

#print "sentences(p): "
#sentences(p)

def sentencesToTranslate(params):
    s = sentences(params)
    word = params['word']
    output = []
    
    for i in s:
        if word in i.split():
            output.append(i)

    print output
    return output

print "sentencesToTranslate(p): "
sentencesToTranslate(p)

#returns a list of sentences that contain any of the words that are passed as part of params
def sentencesToTranslate2(params):
    s = sentences(params)
    words = params['words']
    output = []
    
    for i in s:
        for word in words:
            if word in i.split():
                if not(i in output):
                    output.append(i)

    print output
    return output

print "sentencesToTranslate2(p): "
sentencesToTranslate2(p)
