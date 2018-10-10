import math
n = 1
s = 0
a = ((2*n)**3)/2**n 
while a >= 10**(-4):    
    s += a
    n += 1
    a = ((2*n)**3)/2**n    
print('s = ', s)
print('a_n = %2.7f' % a)
print('kilkist iteracii = ', n)
    
