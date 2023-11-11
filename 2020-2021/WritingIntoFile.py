readfile = open('Employees.txt','r')
writefile = open('Employee_Bonus','w')
lines = readfile.readlines()
for line in lines:
   linesplit = line.split(',')
   value = int(linesplit[-1][:-1])*(1.05)
   writefile.write(linesplit[0]+','+linesplit[1]+','+str(int(value))+'\n')
writefile.close()
readfile.close()
