user_input = int(input('Enter the length of the sequence: '))
fibonacci_list = []
def FibonacciFunction(number):
   if number <= 1:
       return number
   else:
       return(FibonacciFunction(number-1) + FibonacciFunction(number-2))
print("The fibonacci sequence of the length",user_input, "is: ")
for i in range(user_input):
    temp = FibonacciFunction(i) 
    fibonacci_list.append(temp)
print(fibonacci_list)
