fruits = ["사과", "바나나", "체리", "포도", "딸기"]
for fruit in fruits:
    print(fruit)

print(", ".join(fruits))

role = """
===> 학생 5명의 이름을 리스트에 저장하고 for문으로 전체 출력해 보세요.
"""
print(role)
students = ["홍길동", "김철수", "이영희", "박지민", "최성준"]
for student in students:
    print(student)
print(", ".join(students))
print(students)

role = """
나 엔드하고나서 별표로 할꺼야
"""
for student in students:
    print(student, end = "*")

role = """
나 엔드하고나서 별표로 할꺼야, 단 마지막에는 별표 안붙게 할꺼야
"""
print(role)
for student in students:
    print(student, end = "*" if student != students[-1] else "\n")
print("*".join(students))

role = """
===> 학생 점수 10개 저장된 리스트를 for문으로 전체 출력하고, 평균을 구해서 출력해 보세요.
"""
print(role)
scores = [85, 90, 78, 92, 88, 76, 95, 89, 84, 91]
total = 0
for score in scores:
    print(score)
    total += score
print(f"총점: {total}")
print(f"평균: {total / len(scores)}")

role = """
===> 학생들의 점수들을 10단위로 구간을 나누어 몇명인지 출력해 보세요.
"""
print(role)
scores = [85, 90, 78, 92, 88, 76, 95, 89, 84, 91]
grade_counts = [0] * 10  # 0-9점, 10-19점, ..., 90-99점, 100점

for score in scores:
    grade = score // 10
    grade_counts[grade] += 1

for i, count in enumerate(grade_counts):
    if count > 0:
        print(f"{i * 10}-{i * 10 + 9}: {count}명")

"""
print(f"{role}, pandas를 이용해서도 할 수 있어요")
scores = [85, 90, 78, 92, 88, 76, 95, 89, 84, 91]
import pandas as pd

# pandas를 이용한 간단한 구간별 집계
s = pd.Series(scores)
counts = (s // 10).value_counts().sort_index()
for grade, cnt in counts.items():
    if cnt > 0:
        print(f"{int(grade) * 10}-{int(grade) * 10 + 9}: {cnt}명")
"""

for n in range(1, 10): # range(1, 10) : 1부터 9까지 값을 얻어옴
    print(n, end = " ")

# 학생점수 입력받아 출력하는 작업을 5번 반복하는 for문 작성
# for _ in range(5):
#     score = int(input("학생 점수를 입력하세요: "))
#     print(f"입력된 점수: {score}")
print() # 줄바꿈

# 1부터 100까지 for를 이용해서 출력해 보세요 range 함수 사용
print("===> 1부터 100까지 for를 이용해서 출력해 보세요 range 함수 사용")
for n in range(1, 101):
    print(n, end = " ")
print() # 줄바꿈

# 1부터 100까지 수중에 짝수 출력하기
print("===> 1부터 100까지 수중에 짝수 출력하기")
for n in range(1, 101):
    if n % 2 == 0:
        print(n, end = " ")
print() # 줄바꿈

role = """
===> 1부터 100까지 수 출력하기
단 한줄에 10개씩 출력하기
"""
print(role)
for n in range(1, 101):
    print(n, end = " ")
    if n % 10 == 0:
        print() # 줄바꿈

role = """
===> 구구단 표 예쁘게 출력하기
"""
print(role)
for j in range(1, 10):
    print("|".join(f"{i}x{j}={i * j:2}" for i in range(2, 10)))

role = """
===> 1부터 100까지 수의 합 구하기
"""
print(role)
total = 0
for n in range(1, 101):
    total += n
print(f"1부터 100까지 수의 합: {total}")

role = """
===> 1부터 100까지 수의 합 구하기(코드 최대 간결하게)
"""
print(role)
print(f"1부터 100까지 수의 합: {sum(range(1, 101))}")
