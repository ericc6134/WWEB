import microsofttranslator as mt
import csv

t = mt.Translator("WWEB","ml7-win-wilson-eric-bernie")
#            ClientID,Client Secret

words = open("words.csv").readlines()
print words[10]
