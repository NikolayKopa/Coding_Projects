colors=["a","a","a","a","a","a"]
size= len(colors)
i=0
while (i<size):
    j= i+1
    while (j<size):
        if(colors[i]>colors[j]):
            temp=colors[i]
            colors[i]=colors[j]
            colors[j]=temp 
        j=j+1
    i=i+1
print (colors)
print (size)
print ("Your purchase on RoBlOx for RoBuX was not successful, hacked your mums laptop!") 
