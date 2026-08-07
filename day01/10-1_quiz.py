quiz_1 = """
===> 퀴즈1. 변수 temperature가 30 이상이면 "덥습니다"를, 그렇지 않으면 "괜찮습니다"를 출력하는 if문을 작성하세요.
"""
print(quiz_1)
def check_temperature(temp):
    return "덥습니다" if temp >= 30 else "괜찮습니다"
input_temp = int(input("온도를 입력하세요: "))
result = check_temperature(input_temp)
print(f"온도체크 결과: {result}")

quiz_2 = """
===> 퀴즈2. 변수 age가 65 이상이면 "경로우대", 19세 이상이면 "성인", 그 외에는 "미성년자"를 출력하는 if-elif-else문을 작성하세요.
"""
print(quiz_2)
def check_age_group(age):
    if age >= 65:
        return "경로우대"
    elif age >= 19:
        return "성인"
    else:
        return "미성년자"
input_age = int(input("나이를 입력하세요: "))
result = check_age_group(input_age)
print(f"결과: {result}")

quiz_3 = """
===> 퀴즈3. 변수 id가 "admin"이고, 변수 pw가 "1234"일 때만 "로그인 성공"을 출력하고, 그 외에는 "로그인 실패"를 출력하는 if문을 작성하세요. (and 연산자 사용)
"""
print(quiz_3)
input_id = input("아이디를 입력하세요: ")
input_pw = input("비밀번호를 입력하세요: ")
def check_login(id, pw):
    return "로그인 성공" if id == "admin" and pw == "1234" else "로그인 실패"
result = check_login(input_id, input_pw)
print(f"로그인 결과: {result}")

quiz_4 = """
===> 퀴즈4. 변수 stock(재고 수량)이 0이면 "품절", 10 미만이면 "재고 부족", 그 외에는 "재고 충분"을 출력하는 if-elif-else문을 작성하세요.
"""
print(quiz_4)
input_stock = int(input("재고 수량을 입력하세요: "))
def check_stock(stock):
    if stock == 0:
        return "품절"
    elif stock < 10:
        return "재고 부족"
    else:
        return "재고 충분"
result = check_stock(input_stock)
print(f"재고 상태: {result}")

quiz_5 = """
===> 퀴즈5. 리스트 cart = ["우유", "빵", "계란"]에 "계란"이 포함되어 있으면 "장바구니에 계란이 있습니다"를 출력하는 if문을 작성하세요. (in 연산자 사용)
"""
print(quiz_5)
cart = ["우유", "빵", "계란"]
input_item = input("장바구니에 있는지 확인할 아이템을 입력하세요: ")
def check_cart(item):
    return "있습니다" if item in cart else "없습니다"
result = check_cart(input_item)
print(f"장바구니 확인: {input_item}는/은 장바구니에 {result}")
