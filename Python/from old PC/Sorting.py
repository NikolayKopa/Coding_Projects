number_list = []

amount = int(input("How many values will be in the list?: "))

number_list = list(map(int,input("\nEnter the numbers seperated by space : ").strip().split()))[:amount]

for i in range (amount):
    for j in range(i + 1, amount):
        if(number_list[i] > number_list[j]):
            temp = number_list[i]
            number_list[i] = number_list[j]
            number_list[j] = temp

print("Element After Sorting List in Ascending Order is : ", number_list)
