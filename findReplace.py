import re
import urllib
#import translate
#import nltk

def getPage(url):
    file = urllib.urlopen(url)
    raw = file.read()
    s = str(raw)
    
    return s
    
#opens the text file and returns it as one string
def openText(txt):
    l = open(txt).readlines()
    l = str(l)

    return l

def stringify(lst):
    s = ""
    for line in lst:
        s = s + line

    return s

def cleanUp(txt):        
#removes most of the unwanted text (and some of the post, but only links)
    blockRemove = re.compile('<( )*?[Ss]cript.*?</( )*?[Ss]cript( )*?>|<( )*?[Tt]itle.*?</( )*?[Tt]itle( )*?>|<( )*?head.*?</( )*?head( )*?>|<( )*?ul.*?</( )*?ul( )*?>|<( )*?[Ll]ink.*?</( )*?[Ll]ink( )*?>|<( )*?h6.*?</( )*?h( )*?>|<( )*?h5.*?</( )*?h5( )*?>|<( )*?[Ss]pan.*?</( )*?[Ss]pan( )*?>|<( )*?a.*?</( )*?a( )*?>')
    txt = re.sub(blockRemove,"",txt)
        
    tagRemove = re.compile('<.*?>')
    txt = re.sub(tagRemove,"",txt)

    #charRemove = re.compile('[^ A-Za-z]+')
    #text = re.sub(charRemove,"",txt)

    charfix = re.compile('&[rl]dquo;')
    txt = re.sub(charfix,'"',txt)

    return txt

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

#the following finds all sentences rather than trying to pick out only sentences with the word
def sentences(params):
    t = params['text']
    
    sentenceFind = re.compile('([A-Z][^\.?!";:]*[\.?!])')
    found = re.findall(sentenceFind,t)
    
    return found

def sentencesToTranslate(params):
    s = sentences(params)
    word = params['word']
    output = []
    
    for i in s:
        if word in i.split():
            output.append(i)

    print output
    return output

#returns a list of sentences that contain any of the words that are passed as part of params
def sentencesToTranslate2(params):
    s = sentences(params)
    words = params['words']
    output = []
    
    for sent in s:
        for w in words:
            if w in sent.split():
                print "sent.split(): " + str(sent.split())
                if not(sent in output):
                    output.append(sent)

    print output
    return output

#params must include the orignal text as 'text', and a list of tuples with the original sentence at s[0] and the translated sentence at s[1] as 'sentences'
def replace(params):
    oldText = params['text']
    sentences = params['sentences']
    newText = ""
    
    for s in sentences:
        findOld = re.compile(str(s[0]))
        newText = re.sub(findOld,str(s[1]),oldText)
        oldText = newText
        
    return newText

def placeHolder(params):
    params['output'] = []
    for s in params['sentencesToTranslate']:
        tokens = s.split()
        for word in params['words']:
            for i in tokens:
                if i.lower() == word:
                    tokens[i] = "placeHolder"
        t = ""            
        for i in tokens:
            t = t + i " "
            
        params['output'].append([s,t])
    
    return params
#takes params as a parameter which must include a url, text, or string, as well as a word list
def newPage(params)
    if params['url']:
        s = getPage(params['url'])
    elif params['text']:
        s = openText(params['url'])
    elif params['string']:
        s = params['string']
    else:
        return "Error: Nothing to translate"
    
    words = params['words']
    text = cleanUp(stringify(s))
    
    p = {'words': words, 'text': text, 'sentencesToTranslate': []}
    sentences = sentencesToTranslate2(p)
    p['sentencesToTranslate'] = sentences
    
    #at this point p will be sent to the translate code
    #newData = translate.doSomething(p)
    
    p = placeHolder(p)
    
    #this method is not done, for now it returns p; eventually it will return the new page as a string
    return p

b = {'words': ["bomb","Boston"],'word': "nada", 'text':cleanUp(stringify(openText("boston.txt")))}


#print b['text']
print "sentences(b): "
sentences(b)
print "sentencesToTranslate2(b): "
sentencesToTranslate2(b)
