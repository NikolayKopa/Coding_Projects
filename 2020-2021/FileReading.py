inputFile = open("inputFile.txt","r")
a = inputFile.read()
inputFile.seek (0)
a = inputFile.readlines()
inputFile.seek(0)
for a in inputFile:
    print("The word 'the' occurs this many times in your paragraph:")
inputFile.seek (0)
inputFile.close() 
with open("inputFile.txt","r") as inp, open("out.txt", "w") as out:
    for i in inp:
        out.write(i)
stringParagraph = a
word = "the"
words = stringParagraph.lower().split()
wordCount = 0
for w in words:
   if w == word:
      wordCount += 1
print(wordCount)
