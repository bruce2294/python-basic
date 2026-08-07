money = 1000
print(f"현재 잔액 => {money}")
while money > 0:
    n = int(input("얼마짜리 살거야?: "))
    if n > money:
        print("잔액이 부족해~")
        print(f"잔액 => {money}")
        continue
    money -= n
    print(f"남은 잔액 ==> {money}")
