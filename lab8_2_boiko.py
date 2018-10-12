def f(*args):
    n = 1
    ls = []
    for x in args:
        if max(args) > sum(args):
            ls.append(1)
        else:
            ls.append(0)
        n += 1
    if sum(args) > 0 :
        return 0
    else:
        d = 1
        for x in args:
            d += x
        return d
    
x = [99,2,3,7]
res = f(*x)
print('f({}) = {}\n'.format(x, res))
        
            
