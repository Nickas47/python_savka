while(1 == 1):
    s = str(input())
    k=0
    for x in s:
        if(x in '1234567890'):
            k = k + 1
    print(k)
