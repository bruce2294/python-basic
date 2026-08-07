"""
**퀴즈1.** 변수 `num`을 1부터 시작해서 5가 될 때까지 출력하는 while문을 작성하세요. (1, 2, 3, 4, 5 출력)

**퀴즈2.** 변수 `money`가 10000원 있을 때, 1000원씩 계속 사용해서 0원이 될 때까지 남은 금액을 출력하는 while문을 작성하세요.

**퀴즈3.** 1부터 100까지의 숫자를 while문으로 모두 더한 합계를 구해서 출력하세요.

**퀴즈4.** 무한 반복(`while True`)을 사용하되, 변수 `num`이 0부터 시작해서 짝수일 때만 출력하고, num이 10이 되면 `break`로 반복을 종료하는 while문을 작성하세요.

**퀴즈5.** 리스트 `stock = ["사과", "바나나", "포도"]`에서 리스트가 빌 때까지 하나씩 꺼내 "판매완료: OO" 형식으로 출력하는 while문을 작성하세요. (pop() 활용)
"""

quiz_1 = """
퀴즈1. 변수 num을 1부터 시작해서 5가 될 때까지 출력하는 while문을 작성하세요. (1, 2, 3, 4, 5 출력)
"""
print(quiz_1)
num_list = list(range(1, 6))
while num_list:
    num = num_list.pop(0)
    print(num, end=", ") if not num == 5 else print(num)

quiz_2 = """
퀴즈2. 변수 money가 10000원 있을 때, 1000원씩 계속 사용해서 0원이 될 때까지 남은 금액을 출력하는 while문을 작성하세요.
"""
print(quiz_2)
money = 10000
while money > 0:
    print(f"잔액: {money}")
    money -= 1000

quiz_3 = """
퀴즈3. 1부터 100까지의 숫자를 while문으로 모두 더한 합계를 구해서 출력하세요.
"""
print(quiz_3)
total = 0
num_list = list(range(1, 101))
while num_list:
    total += num_list.pop(0)
print(f"total: {total}")

quiz_4 = """
퀴즈4. 무한 반복(while True)을 사용하되, 변수 num이 0부터 시작해서 짝수일 때만 출력하고, num이 10이 되면 break로 반복을 종료하는 while문을 작성하세요.
"""
print(quiz_4)
num = 0
while True:
    if num % 2 == 0:
        print(num)
    if num == 10:
        break
    num += 1

quiz_5 = """
퀴즈5. 리스트 stock = ["사과", "바나나", "포도"]에서 리스트가 빌 때까지 하나씩 꺼내 "판매완료: OO" 형식으로 출력하는 while문을 작성하세요. (pop() 활용)
"""
print(quiz_5)
stock = ["사과", "바나나", "포도"]
while stock:
    sale = stock.pop(0)
    print(f"{sale} 판매 완료, 재고: {stock}")
