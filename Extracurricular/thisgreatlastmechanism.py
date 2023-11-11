file = open("thenames.txt","r")
i = 0
readlines = file.readlines()
while(i<(readlines)):
    j = i+1
    while(j<(readlines)):
        if(readlines[i]>readlines[j]):
            temp = readlines[i]
            readlines[i] = readlines[j]
            readlines[j] = temp
        i = i+1
    j = j+1
print(readlines)
file.close()
theAges = open("theagesofnames.txt","r")
readAges = theAges.readlines()
i2 = 0
while(i<(theAges)): 
    j = i+1
    while(j<(theAges)):
            if(readAges[i2]>readAges[j]):
               temp2 = readAges[i]
               readAges[i] = readAges[j]
               readAges[j] = temp2
            i = i+1
    j = j+1
    print(readlines)
theAges.close()
