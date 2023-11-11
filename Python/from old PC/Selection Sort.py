def selection(numberlist):
   for i in range(len(numberlist)-1):
       minimum_index = i
       for j in range(i+1, len(numberlist)):
           if numberlist[minimum_index] > numberlist[j]:
               minimum_index = j
       numberlist[i], numberlist[minimum_index] = numberlist[minimum_index], numberlist[i]
   return numberlist

numberlist = input('Type in some numbers in random order(split with commas): ').split(',')

for i in range(len(numberlist)):
   numberlist[i] = int(numberlist[i])

print(selection(numberlist))
