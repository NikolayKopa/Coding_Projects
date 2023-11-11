string = input("What should the string be?")
sum = 0
vowels = ['a','e','i','o','u','A','E','I','O','U']
for char in vowels:
    freq = string.count(char)
    if freq > 0:
        print('Number of ' + str(char) + ': ' + str(freq))
    sum += ord(char)*freq
print('Total ASCII Value: ' + str(sum))
