import removeVowelsFunction
inputFile = open('rem_vowels_input.txt','r')
outputFile = open('rem_vowels_output.txt','w')
words = inputFile.read()
words = words.lower()
vowelsList = ['a','e','i','o','u']
for v in vowelsList:
   words = removeVowelsFunction.removeWithout(words,v)
outputFile.write(words)
inputFile.close()
outputFile.close()
