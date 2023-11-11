names=[Nick,John,Fork]
ages=[56,4,234] 
sizeone= len(names)
sizetwo= len(ages)
i=0
print (names)
print (ages) 
while (i<sizeone):
    j= i+1
    while (j<sizeone):
        if(names[i]>names[j]):
            tempone=names[i]
            temptwo=ages[i]
            names[i]=names[j]
            ages[i]=ages[j] 
            names[j]=tempone
            ages[j]=temptwo 
        j=j+1
    i=i+1
print (names) 
print (ages) 
    
