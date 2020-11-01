def gugudan(dan):
    number = [1,2,3,4,5,6,7,8,9]
    a = dan
#    if a == 3: continue
    for b in number:
        c = a * b
        print('{} * {} = {}'.format(a,b,c))

    return b
k = int(input("몇 단을 실행할까요?"))
result = gugudan(k)
print(result)