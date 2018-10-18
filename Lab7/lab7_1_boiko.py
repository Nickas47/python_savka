import random
k=0
while(k < 10):
    god = random.randrange(0,23,1)
    hv = random.randrange(0,59,1)
    s = random.randrange(0,59,1)
    k=k+1
    print('{}:{}:{}'.format(god, hv, s))
god1 = random.randrange(0,23,1)
god2 = random.randrange(0,23,1)
hv1 = random.randrange(0,59,1)
hv2 = random.randrange(0,59,1)
s1 = random.randrange(0,59,1)
s2 = random.randrange(0,59,1)

if god1 < god2:
    print('\nперша година раніше')
elif god1 > god2:
     print('\nдруга година раніше')
elif (god1 == god2) and (hv1 < hv2):
    print('\nперша година раніше')
elif (god1 == god2) and (hv1 > hv2):
     print('\nдруга година раніше')
elif (god1 == god2) and (hv1 == hv2) and (s1 < s1):
    print('\nперша година раніше')
elif (god1 == god2) and (hv1 == hv1) and (s1 > s1):
     print('\nдруга година раніше')
print('{}:{}:{}'.format(god1, hv1, s1))
print('{}:{}:{}'.format(god2, hv2, s2))
