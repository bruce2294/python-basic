quiz_1 = """
퀴즈1. 딕셔너리 product = {"name": "노트북", "price": 1200000}을 만들고, name과 price 값을 각각 출력하세요.
"""
print(quiz_1)
product = {"name": "노트복", "price": 1200000}
# for item in product.items():
#     print(f"{item[0]}: {item[1]}")
print(", ".join(str(dict_val) for dict_val in product.values()))

quiz_2 = """
퀴즈2. product 딕셔너리에 "stock": 5 를 새로운 키-값으로 추가하고 출력하세요.
"""
print(quiz_2)
product["stock"] = 5
print(", ".join(str(dict_val) for dict_val in product.values()))

quiz_3 = """
퀴즈3. 딕셔너리 user = {"id": "hong123", "email": "hong@example.com"}에서 get()을 사용해 "phone" 키를 조회하되, 값이 없으면 "등록된 번호 없음"을 반환하도록 작성하세요.
"""
print(quiz_3)
user = {"id": "hong123", "email": "hong@example.com"}
phone = user.get("phone")
print(phone if not phone is None else "등록된 번호 없음")

quiz_4 = """
퀴즈4. 딕셔너리 scores = {"수학": 90, "영어": 85, "과학": 95}를 for문과 .items()를 사용해 "수학: 90" 형식으로 모두 출력하세요.
"""
print(quiz_4)
scores = {"수학": 90, "영어": 85, "과학": 95}
print(f"items type: {type(scores.items())}")
for item in scores.items():
    # print(": ".join(str(score) for score in item))
    print(f"{item[0]}: {item[1]}")

quiz_5 = """
퀴즈5. 딕셔너리 cart = {"사과": 3, "바나나": 5, "포도": 2}에서 수량(value)이 가장 많은 과일의 이름을 찾아 출력하세요. (반복문 활용, max() 사용 금지)
"""
print(quiz_5)
cart = {"사과": 3, "바나나": 5, "포도": 2}
max_fruit = ()
for index, fruit in enumerate(cart.items()):
    if index == 0:
        max_fruit = fruit
    else:
        if fruit[1] > max_fruit[1]:
            max_fruit = fruit
print(": ".join(str(fruit) for fruit in max_fruit))
print(max(cart.values()))

role = """
max 값 구하기 알고리즘
"""
print(role)
a = [10, 30, 90, 60]
num_max = 0
for n in a:
    if n > num_max:
        num_max = n

print(num_max)

print("===> use pandas")
import pandas as pd
df = pd.DataFrame(cart, index=[0])
print(df)
print(f"최댓값 열 이름 (Series): {df.idxmax(axis=1)}")
print(f"최댓값 자체: {df.max(axis=1).iloc[0]}")
print(f"행 하나 기준 접근: {df.iloc[0].idxmax()}")
