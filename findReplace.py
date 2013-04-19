import re
#import nltk

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


b = {'words': ["bomb","Boston"],'word': "nada", 'text':cleanUp(stringify(openText("boston.txt")))}


#print b['text']
print "sentences(b): "
sentences(b)
print "sentencesToTranslate2(b): "
sentencesToTranslate2(b)
