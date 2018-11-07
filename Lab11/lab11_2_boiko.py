import math
def gen(x,epsilon):
    k = 0
    x_k = 1
    while True:
         yield x_k
         v = math.pow(x,2)/((2*k+1)*(2*k+2))
         x_k = x_k * v
         k += 1
         if math.fabs(x_k)<epsilon:
             return StopIteration
              
x = float(input("x = "))
epsilon = float(input("epsilon = "))
s = 0
for x in gen(x, epsilon): 
    s+=x
    print(s)
