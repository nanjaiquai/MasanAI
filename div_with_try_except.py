#try_with_except.py

try:
    a, b, c = input('세 수를 입력하시오: ').split()
    result = int(a) / int(b) / int(c)
    print('{}/{}/{} = {}'.format(a, b, c, result))
except Exception as e:
    print('수가 정확한지 확인하세요.')