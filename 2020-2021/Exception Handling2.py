user_input = input('Type in a list of numbers split by commas: ').split(',')
factorial_list  = []
for i in range(len(user_input)):
  if i >= len(user_input) or i < 0:
      print("The index is out of range!")
  factorial_total = 1
  for n in range(1,int(user_input[i])+1):
      factorial_total *= n
  factorial_list.append(factorial_total)
print(factorial_list)
