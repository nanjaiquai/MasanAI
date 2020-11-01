number = [1,2,3,4,5,6,7,8,9]
dan = [1,2,3,4,5,6,7,8,9]
for a in dan:
    if a == 3: continue
    for b in number:
        c = a * b
        print(a," X" ,b, "=" ,c)
        print('\n')
        print('{} * {} = {}'.format(a,b,c))
        print('%d'%(a*b))