import math
a = 1
s = 0
x = math.sqrt(a)
x_n  = 1/2*(x+a/x) 
while a >= 10**(-4):    
    s += x_n
    x += Math.sqrt(a)
    x_n  = 1/2*(x+a/x)    
print('s = ', s)
print('a_n = %2.7f' % a)
print('kilkist iteracii = ', n)
    
