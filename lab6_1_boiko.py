a = list(input('List: '))
print(a)
x = input('x: ')
a.append(x)
for i in range(len(a), 0, -1):
    for j in range(0, len(a) - 1):
        if a[j] > a[j+1]:
            a[j], a[j+1] = a[j+1], a[j]
             
print(a)
