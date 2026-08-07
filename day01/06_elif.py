score = 85
def get_lever(score):
    if score == 100:
        lever = "S"
    elif score >= 90:
        lever = "A"
    elif score >= 80:
        lever = "B"
    elif score >= 70:
        lever = "C"
    elif score >= 60:
        lever = "D"
    else:
        lever = "F"
    return lever

lever = get_lever(score)

print(f"점수 : {score}, 등급 : {lever}")

a = """
아리랑
아리랑
아라리요
"""
print(a)

"""
여기서 주석 여러줄
나이를 입력받아
나이가 10살 이하이면 어린이
나이가 19살 이하이면 청소년
나이가 20살 이상이면 성인
"""

role = """
===> 나이를 입력받아
나이가 10살 이하이면 어린이
나이가 19살 이하이면 청소년
나이가 20살 이상이면 성인
"""
print(role)
age = int(input("나이를 입력하세요: "))
def get_age_group(age):
    if age <= 10:
        group = "어린이"
    elif age <= 19:
        group = "청소년"
    else:
        group = "성인"
    return group

age_group = get_age_group(age)
print(f"나이 : {age}, 그룹 : {age_group}")

role = """
===> 정수를 입력받아 입력받은 수가 짝수인지/홀수인지 판별하기
"""
print(role)
num = int(input("정수를 입력하세요: "))
def is_even_odd(num):
    if num % 2 == 0:
        result = "짝수"
    else:
        result = "홀수"
    return result

result = is_even_odd(num)
print(f"입력한 수 : {num}, 결과 : {result}")
