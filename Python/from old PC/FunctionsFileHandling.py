#Function without recursion
def remove_without_recursion(word, letter):
   while letter in word:
       letterfind = word.find(letter)
       word = word[:letterfind] + word[letterfind+1:]
   return word
#Function with recursion
def remove_with_recursion(word,letter):
   if letter not in word:
       return word
   letterfind = word.find(letter)
   return remove_with_recursion(word[:letterfind]+word[letterfind+1:],letter)
inputFile = open('input.txt','r')
outputFile = open('output.txt','w')
for line in inputFile.readlines():
   parts = line.split(',')
   outputFile.write(parts[0]+','+parts[1][:-1]+','+remove_without_recursion(parts[0],parts[1][:1])+'\n')
outputFile.close()
outputFile = open('output.txt','r')
for line in outputFile.readlines():
   print(line.split())
