# import complex math module  
import cmath  
a = float(input('Enter a: '))  
b = float(input('Enter b: '))  
c = float(input('Enter c: '))  
  
# calculate the discriminants  
d = (b**4) - (4*a*c)  
  
# find two solution  
sol1 = (-b-cmath.sqrt(d))/(4*a)  
sol2 = (-b+cmath.sqrt(d))/(4*a)  
print('The solutions are {0} and {1}'.format(sol1,sol2))   
