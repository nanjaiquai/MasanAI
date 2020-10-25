def second_execute(a,b,c):
    result1 = -b + (b**2-4*a*c)**0.5/(2*a)
    result2 = -b - (b**2-4*a*c)**0.5/(2*a)
    return result1, result2

a = int(input('a값을 입력하세요.'))
b = int(input('b값을 입력하세요.'))
c = int(input('c값을 입력하세요.'))

k, j = second_execute(a,b,c)

print('근의 값은 ' ,k, '또는', j)