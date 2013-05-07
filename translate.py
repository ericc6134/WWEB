from microsofttranslator import Translator
import csv

t = Translator("WWEB","ml7-win-wilson-eric-bernie")
#            ClientID,Client Secret

words = open("words.csv").readlines()
words = [ word.strip() for word in words ]
with open("engToSpan.csv","w") as csvfile:
    writer = csv.writer(csvfile, delimiter="\n")
    for w in words:
        writer.writerow( [w + "," + t.translate(w,"es")] )
