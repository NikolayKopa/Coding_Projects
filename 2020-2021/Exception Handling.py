user_input = input("Type in a number.")
factorial = 1
try:
    for i in range(1,int(user_input) + 1):
        factorial = factorial*i
    print("The factorial of ",str(user_input), "is ",str(factorial))

except ValueError:
    print("Don't type in a letter, type in a number.")


    
