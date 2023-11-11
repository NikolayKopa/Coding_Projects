import math
a=int(input("What should the value of a be? "))
b=int(input("What should the value of b be? "))
c=int(input("What should the value of c be? "))
quadratic_one= b**2 -4 * a * c
if a!=0:
  if quadratic_one>=0:
      x1=(-b+math.sqrt(quadratic_one))/2/a
      x2=(-b-math.sqrt(quadratic_one))/2/a
      root=[x1,x2]
      sorted_roots=sorted(root)
      if x1!=x2:
          answer = "Yes "+format(sorted_roots[0],'.2f')+" "+format(sorted_roots[1],'.2f')
      else:
          answer = "Yes "+format(x1,'.2f')
  else:
      answer = "No"
print (answer) 
