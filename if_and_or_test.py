a = int(input("첫번째 숫자를 입력해주세요"))
b = int(input("두번째 숫자를 입력해주세요"))

if a % 2 == 0 and b % 2 == 0 :
    print("두 수 모두 짝수입니다")
elif a % 2 != 0 and b % 2 == 0 :
    print("첫번째는 홀수, 두번째는 짝수입니다")
elif a % 2 == 0 and b % 2 != 0 :
    print("첫번째는 짝수, 두번째는 홀수입니다")
elif a % 2 != 0 and b % 2 != 0 :
    print("두 수 모두 홀수입니다")