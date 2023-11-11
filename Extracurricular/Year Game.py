def calcAge (birthyear, yearnow):
    return yearnow-birthyear
yearnow = int(input("Type what year it is"))
birthyear = int(input("Type the year you were born in"))
age = calcAge (birthyear, yearnow)
print("Your" , age)
