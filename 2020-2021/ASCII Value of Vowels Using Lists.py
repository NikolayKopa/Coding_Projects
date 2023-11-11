vowels = ['a','e','i','o','u','A','E','I','O','U']
sentence = input("Type a sentence.")
asciiVal = 0
vowelCount = {
   'a' : 0,
   'e' : 0,
   'i' : 0,
   'o' : 0,
   'u' : 0,
   'A' : 0,
   'E' : 0,
   'I' : 0,
   'O' : 0,
   'U' : 0,
   }

for i in sentence:
   for j in vowels:
       if i == j:
           asciiVal += ord(i)
           vowelCount[j] += 1
print(asciiVal)
for i in vowels:
   if vowelCount[i] > 0:
       print(i, "=", vowelCount[i])
