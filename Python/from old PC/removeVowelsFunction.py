def removeWith(letter,word):
   if letter not in word:
       return word
   n = word.find(letter)
   return remove_with(word[:n]+word[n+1:],letter)
def removeWithout(words,character):
   while character in words:
       n = words.find(character)
       words = words[:n] + words[n+1:]
   return words
if __name__ == "__main__":
   inputFile = open('input.txt','r')
   outputFile = open('output.txt','w')
   for line in inputFile.readlines():
       portions = line.split(',')
       outputFile.write(portions[0]+','+portions[1][:1]+','+remove_with(portions[0],portions[1][:1])+'\n')
       outputFile.write(portions[0]+','+portions[1][:1]+','+remove_without(portions[0],portions[1][:1])+'\n')
   outputFile.close()
