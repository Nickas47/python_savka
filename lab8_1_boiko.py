'''Python: Lab8
Mykola Boiko, pm-12343'''
print("'Python': Lab8 \n Mykola Boiko, pm-12343")
def han (n,a,b,c):
    if n != 0:
        han(n-1,a,c,b)    
        print('{} -> {}'.format(a,b))  
        han(n-1,c,b,a)    

n = int(input("введіть кількість дисків: "))

han(n,1,2,3)
