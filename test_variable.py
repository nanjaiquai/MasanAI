a = [1,2,3]
print(a)
print(a[0])
print(a[-1])

a = [1,2,3, ['a', 'b', 'c']]
print(a)
print(a[0])
print(a[-1])

def abc(*args):
    return args[1], args[0], args[2]
print(abc(*(1,5,9,11)))

abc(*(1,5,9,11,33,55,77))


def sum_all(*args):
    result = 0
    for i in args:
        result += i

    return result

print(sum_all(1,2,3,4,5))
print(sum_all(1,2,3,4,5,6,7,8,9,10))

def abc(a, *args):
    return args[0], a, args[1]

abc(*(1,5,9))
