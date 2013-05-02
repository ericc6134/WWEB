import microsofttranslator
import csv

t = microsofttranslator.Translator.Translator("WWEB","ml7-win-wilson-eric-bernie")
#            ClientID,Client Secret

words = open("words.csv").readlines()
print words
