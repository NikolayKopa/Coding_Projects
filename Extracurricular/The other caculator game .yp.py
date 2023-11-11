def add(num1,num2):
    return num1+num2
def sub(num1,num2):
    return num1-num2
def mul(num1,num2):
    return num1*num2
def div(num1,num2):
    return num1/num2
operation = input ("Tell me if I should multiply, divide, add or subtract")
num1 = int(input("Give me a number"))
num2 = int(input("Give me another number"))
if operation == "add":
    print (add(num1, num2))
if operation == "subtract":
    print (sub(num1, num2))
if operation == "multiply":
    print (mul(num1, num2))
if operation == "divide":
    print (div(num1, num2))
