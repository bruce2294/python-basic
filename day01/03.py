a = 10
b = 4
print(f"{a} + {b} = {a + b}")
print(f"{a} - {b} = {a - b}")
print(f"{a} * {b} = {a * b}")
print(f"{a} / {b} = {a / b}")
print(f"{a} // {b} = {a // b}") # 몫
print(f"{a} % {b} = {a % b}")   # 나머지
print(f"{a} ** {b} = {a ** b}") # 거듭제곱

# 이름, 국어, 영어 점수 입력받아 이름과 총점을 구해서 출력하기
name = input("이름을 입력하세요: ")
kor = int(input("국어 점수를 입력하세요: "))
eng = int(input("영어 점수를 입력하세요: "))
total = kor + eng
subject_count = 2
avg = total / subject_count
# 평균이 정수면 정수형으로, 아니면 실수형으로 표시
avg_display = int(avg) if (avg % subject_count == 0) else round(avg, 2)
# 입력된 이름과 국어점수/영어점수를 출력해 보세요
# 이름 : 홍길동
# 국어점수 : 100
# 영어점수 : 50
print(f"이름 : {name}")
print(f"국어점수 : {kor}")
print(f"영어점수 : {eng}")
print(f"{name}님의 총점은 {total}점 입니다.")
print(f"{name}님의 {subject_count}과목 평균은 {avg_display}점 입니다.")
