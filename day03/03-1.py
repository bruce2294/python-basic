email = "student@example.com"

print(email.endswith("@example.com"))    # True
print(email.startswith("student"))       # True
print(email.endswith(".net"))            # False

print(email.find("example") > -1)


import re

text = "제 전화번호는 010-1234-5678입니다"

# 숫자 패턴 포함 여부
if re.search(r'\d{3}-\d{4}-\d{4}', text):
    print("전화번호 패턴이 존재합니다")


text = "Hello Python"

print(text.upper())    # HELLO PYTHON
print(text.lower())    # hello python

text = "   파이썬 공부   "

print(text.strip())     # "파이썬 공부"
print(text.lstrip())    # "파이썬 공부   "
print(text.rstrip())    # "   파이썬 공부"

text = "저는 자바를 배웁니다"

new_text = text.replace("자바", "파이썬")
print(new_text)    # 저는 파이썬을 배웁니다

phone = "010-1234-5678"
print(phone.replace("-", ""))    # 01012345678

text = "사과,바나나,포도"
fruits = text.split(",")
print(fruits)    # ['사과', '바나나', '포도']

sentence = "저는 파이썬을 배웁니다"
words = sentence.split()    # 기준문자를 생략하면 공백 기준으로 나눔
print(words)    # ['저는', '파이썬을', '배웁니다']

fruits = ["사과", "바나나", "포도"]
result = ", ".join(fruits)
print(result)    # 사과, 바나나, 포도

text = "저는 파이썬을 좋아하는 파이썬 개발자입니다"

print(text.find("파이썬"))     # 3  (처음 등장하는 위치의 인덱스)
print(text.count("파이썬"))    # 2  (등장 횟수)
print(text.find("자바"))       # -1 (없으면 -1 반환)

email = "student@example.com"

print(email.endswith("@example.com"))    # True
print(email.startswith("student"))       # True
print(email.endswith(".net"))            # False

filename = "report.pdf"

if filename.endswith(".pdf"):
    print("PDF 파일입니다.")
else:
    print("PDF 파일이 아닙니다.")

text = "파이썬"
print(len(text))    # 3

password = "abc123"

if len(password) < 8:
    print("비밀번호는 8자 이상이어야 합니다.")

name = "홍길동"
age = 25

print(f"제 이름은{name}이고, 나이는{age}살입니다.")
# 출력: 제 이름은 홍길동이고, 나이는 25살입니다.

email = "  Hong_GilDong@Example.COM  "
role = """
1. `email`의 앞뒤 공백을 제거해 보세요.
2. 공백을 제거한 값을 모두 소문자로 바꿔 보세요.
3. `@` 기준으로 아이디 부분(`hong_gildong`)만 잘라내 보세요. (split 활용)
"""
step1 = email.strip()
print(step1)
step2 = step1.lower()
print(step2)
step3 = step2.split("@")[0]
print(step3)

print("===> 예시 2 - sorted()와 람다 함께 사용")
students = [("철수", 85), ("영희", 92), ("민수", 78)]

sorted_students = sorted(students, key=lambda x: x[1], reverse=1)
print(sorted_students)