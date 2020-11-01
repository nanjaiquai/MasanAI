from datetime import datetime as dt
print(dt.now())
print(dir(dt))
print(dt.now().day)
a, b = input('두 수를 입력하시오').split()

if int(b) != 0:    
    result =int(a)/int(b)
else :
    result = 0

print(result)