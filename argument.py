#위치인자
def get_sum(a, b): # 두 수의 합을 반환하는 함수
    result = a + b
    return result # return 문을 사용하여 result를 반환
# 키워드인자
def get_sum_1(a=1, b=2): # 두 수의 합을 반환하는 함수
    result = a + b
    return result

def get_sum_2(c, d,a=1, b=4 ): 
    result1 = a + b
    result2 = c - d
    return result1, result2

# n1 = get_sum(10, 20)
# print('10과 20의 합 =', n1)
# n2 = get_sum(100, 200)
# print('100과 200의 합 =', n2)
n3= get_sum_1()
print(n3)

n4= get_sum_2(5,6,7,8)
print(n4)

def air_line(**kwargs):
    print('출발지는', kwargs['departure'])
    print('도착지는', kwargs['arrival'])
    print('비행시간은', kwargs['flighttime'])
    
air_line(**{'departure': '서울', 'arrival':'프라하','flighttime':'15시간'})

def makeURL(**kargs):
    myURL = "데스크아아나다안"
    for k, v in kargs.items():
        myURL += k + '=' + v + '&'
    
    myURL = myURL.rstrip('&')
    print(myURL)

makeURL(user='psycho', index = '5', page = '10')

def define_suwoni(msg, nick='천재'):
    print("""
 수워니는 어떤사람? 
     - {msg}
 수워니의 별명은?
     - {nick}
 """.format(msg=msg,nick=nick))
 
define_suwoni('키큰사람', '바보')
define_suwoni('잠이 많은 사람')

import time
time.ctime()
'Mon Mar  5 14:57:24 2018'
time.ctime()
'Mon Mar  5 14:57:27 2018'
def show_time(now=time.ctime()):
    print(now)

show_time()
show_time()
show_time()