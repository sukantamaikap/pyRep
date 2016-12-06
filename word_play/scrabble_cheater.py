import string

import scrabble

print "print all words containing uu"
print("we have a scrabble dictionary of size : " + str(len(scrabble.wordList)))
for word in scrabble.wordList:
    if 'uu' in word:
        print word

print "*****************************************"

print "what are all the letters that never appeared doubled"
for letter in string.ascii_lowercase:
    found = False
    for word in scrabble.wordList:
        if letter * 2 in word:
            found = True
            break

    if not found:
        print letter * 2 + " never appears twice in any english word"
print "*****************************************"
