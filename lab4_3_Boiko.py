import math
a = int(input('a='))
x1 = int(input('x1='))
x_n = x1
x_n1  = 1/2*(x+a/x)
k = 1
while abs(x_n1-x_n) >= 10**(-4):    
    k += 1
   print('x{} = {}'.format(k,n_n1))
    x_n = x_n1   
    x_n1  = 1/2*(x+a/x)
 print('sqrt(a) = x{} = {}'.format(k+1,n_n1))
    
