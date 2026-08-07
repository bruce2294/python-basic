from utils import print_line

role = """
lambda 함수
- 익명함수(이름이 없는 함수)
- 주로 간단한 기능을 한 줄로 표현할때 사용
- 'def'를 쓰지 않고도 간단한 함수를 만들어 사용할때 유용

- 형식
 lambda 매개변수1,.. : 표현식
 ==> lambda는 반드시 표현식(expression) 하나만 가질 수 있고, 그 값이 자동으로 return됩니다.
'''
"""
print("===> 예시 2 - sorted()와 함께 사용")
students = [("철수", 85), ("영희", 92), ("민수", 78)]

sorted_students = sorted(students, key=lambda x: x[1])
print(sorted_students)
# [('민수', 78), ('철수', 85), ('영희', 92)]

print_line()
print("===> 예시 3 - map()과 함께 사용")
numbers = [1, 2, 3, 4, 5]
squared = list(map(lambda x: x ** 2, numbers))
print(squared)

print_line()
print("===> 예시 4 - filter()와 함께 사용")
numbers = list(range(1, 11))
even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
print(even_numbers)

print_line()
print("===> 예시 5 - 조건문이 포함된 람다")
classify = lambda x: "짝수" if x % 2 == 0 else "홀수"
print(classify(4))
print(classify(7))

area = lambda r: r ** 2 * 3.14
print(area(3))

a = list(range(1, 10))
b = list(map(lambda x: str(x) + ": 짝수" if x % 2 == 0 else str(x) + ": 홀수", a))
for num in b:
    print(num)
