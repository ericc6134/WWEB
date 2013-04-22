from microsofttranslator import Translator

t = Translator("WWEB","ml7-win-wilson-eric-bernie")
#            ClientID, Client Secret
for w in "It is just a flesh elephant water".split(" "):
    print t.translate(w,"es")

# OBSERVATIONS:

# Each translation deducts from my quota of 2,000,000 characters per month.
# Translating the same word more than once DOES (!!!!!!!) deduct multiple times.
# Translating "water" to "agua" consumes 5 + 4 = 9 characters

# CONCLUSIONS:

# Be very careful with what words we choose to translate. We probably don't get a refill till May 22nd.
