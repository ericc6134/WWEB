from microsofttranslator import Translator
import csv

t = Translator("WWEB","ml7-win-wilson-eric-bernie")
#            ClientID,Client Secret

words = open("words.csv").readlines()
print words
