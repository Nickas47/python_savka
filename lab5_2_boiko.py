n = int(input('N='))
lst = []
for i in range(0,n):
    s = list(str(i))
    if s[-1] == '3':  
        lst.append(int(''.join(s)))
print(lst)
