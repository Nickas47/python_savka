import math
#Python: Lab3
#Mykola Boiko pm-12343
print("'Python': Lab3 \n Mykola Boiko pm-12343")
x = float(input('x = '))
a = float(input('a = '))
if (x-1)**2 and (a+2) != 1 :
    y = (x**3 + 2*a*x+3)/((x-1)**2)+ (math.cos(x**2)/(a+2))
else :
    y = 'Znamennyk = 0'
print(y)
