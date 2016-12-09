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

# all words containing all vowels i.e a, e, i, o, u

print("find words containing all vowels from the dictionary")
count = 0
for word in scrabble.wordList:
    found = True
    for vowel in "aeiou":
        if vowel not in word:
            found = False
    count = count + 1
    if found:
        print("found word no : " + str(count) + " with all vowels " + word)

print "*****************************************"

# find the longest palindrome from the dictionary
print("find the longest palindrome from the dictionary")

#long way
def is_palindrome(word):
    for index in range(len(word)):
        if word[index] != word[-(index+1)]:
            return False
    return True

temporary = ""
for word in scrabble.wordList:
    if is_palindrome(word) and len(temporary) < len(word):
        temporary = word
print("longest palindrome word found last : " + temporary)

# shorter way 
temporary = ""
for word in scrabble.wordList:
    if word == word[::-1] and len(word) > len(temporary):
        temporary = word

print("longest palindrome word found last : " + temporary)
