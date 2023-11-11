user_input = int(input('Enter a positive number: '))
factor_list = []
fibonacci_list = []
def FibonacciFunction(number):
   if number <= 1:
       return number
   else:
       return(FibonacciFunction(number-1) + FibonacciFunction(number-2))
def FactorFunction(x):
   print("The factors of",x,"are: ")
   for i in range(1, x + 1):
       if x % i == 0:
           factor_list.append(i)
   print(factor_list)
if user_input <= 0:
   print("Again, please enter a positive integer: ")
else:
   print("The fibonacci sequence of",user_input, "are: ")
   for i in range(user_input):
       temp = FibonacciFunction(i) 
       fibonacci_list.append(temp)
   print(fibonacci_list)
FactorFunction(user_input)

