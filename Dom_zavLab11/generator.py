def fibgen():
    
    a, b = 1, 1
    while True:
        yield b
        a, b = b, a + b

n = int(input('n= '))
fg = fibgen()
print('Числа Фібоначчі (next)')
for i in range(n):
    print(i+1, next(fg))


