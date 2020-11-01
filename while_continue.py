coffee = int(input("커피몇개주문하실건가요?"))
money = int(input("얼마인가요?"))

while money:
    print("커피 나왔습니다.")
    coffee -= 1
    if coffee % 2 != 0: continue
    print("남은 커피는 %d개입니다." %coffee)
    if coffee == 0:
        print("커피가 절판되었습니다.")
        break
