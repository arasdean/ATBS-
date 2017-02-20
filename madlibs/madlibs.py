#!Python3
# Madlibs project
# Create a Mad Libs program that reads in text files and lets the user add
# their own text anywhere the word ADJECTIVE, NOUN, ADVERB, or VERB appears
# Are list values immutable?
import re

#TODO: open madlibs text to get readlines
madLibsContentFile = open('madlibs.txt')
# #TODO: Run through text for instances of keywords (Should I use regex?)
madLibsLines = madLibsContentFile.readlines()
newParagraph = ''.join(madLibsLines)

# TODO: open mad libs for writing

editMadLibs = open("madlibs.txt", 'w')

nounRegex = re.compile(r'NOUN')
totalNouns = nounRegex.findall(newParagraph)
adjRegex = re.compile(r'ADJECTIVE')
totalAdj = adjRegex.findall(newParagraph)
verbRegex = re.compile(r'VERB')
totalVerb = verbRegex.findall(newParagraph)

print(newParagraph)
for i in range(len(totalAdj)):
    user_adj = input('Adjective: ')
    if user_adj == 'exit':
        break
    else:
        newParagraph = adjRegex.sub(user_adj, newParagraph, count=1)
        print(newParagraph)

for i in range(len(totalNouns)):
    user_noun = input('Noun: ')
    if user_noun == 'exit':
        break
    else:
        newParagraph = nounRegex.sub(user_noun, newParagraph, count=1)
        print(newParagraph)

for i in range(len(totalVerb)):
    user_verb = input('Verb: ')
    if user_verb == 'exit':
        break
    else:
        newParagraph = verbRegex.sub(user_verb, newParagraph, count=1)
        print(newParagraph)


editedMadLibsContent = editMadLibs.write(newParagraph)
madLibsContentFile.close()
editMadLibs.close()

# findWord = re.compile(r'ADJECTIVE')
# userInput = input('replace Adjective: ')
# findWord.sub(userInput, newParagraph)
# print(newParagraph)
#
# #TODO: close madlibs.txt

#TODO: open a new files & write the content to it
#newMLCF = open('madlibsupdated.txt', 'w')
#newMLCF.write(madLibsContentFile)


# testString = 'NOUN NOUN NOUN NOUN'
# totalNouns = nounRegex.findall(testString)
# print(testString)
# for i in range(len(totalNouns)):
#     user_noun = input('Noun: ')
#     testString = nounRegex.sub(user_noun, testString, count=1)
#     print(testString)
