def add_def(a, b):
    return a + b

add_lambda = lambda a, b: a + b

print(add_def(10, 20))
print(add_lambda(10, 20))

def print_line():
    print("-" * 86)

print_line()

role = """
===> 삼항연산자
[참일 때의 값] if [조건식] else [거짓일 때의 값]
"""
print(role)
a = "정답" if add_lambda(10, 20) == 30 else "에러!"
print(a)

age = 20
result = "성인" if age >= 18 else "미성년자"
print(result)

java_role = """
javaint score = 85;
String result = (score >= 80) ? "합격" : "불합격";
System.out.println(result); // 합격 출력
"""
print(java_role)

a = 10
b = "짝수" if a % 2 == 0 else "홀수"
print(b)

a = 10
b = 20
role = """
두 수중에 큰 값 구하기(두 값은 반드시 다르다는 가정)
"""
c = 0
if a > b:
    c = a
else:
    c = b
print(c)

c = a if a > b else b
print(c)

print_line()
if a < b:
    a, b = b, a
print(a)

c = a if a > b else b
print(a)
print(b)
print(c)
