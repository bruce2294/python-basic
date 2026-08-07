role = """
===> 1. 자신의 이름, 나이, 연락처를 입력받아 출력해 보세요
"""
print(role)
name = input("이름을 입력하세요: ")
age = int(input("나이를 입력하세요: "))
phone = input("연락처를 입력하세요: ")

print(f"이름: {name}, 나이: {age}, 연락처: {phone}")

role = """
===> 2. 학생번호와 정수를 입력받아 학점을 구해서 출력해 보세요.
"""
print(role)
student_id = input("학생번호를 입력하세요: ")
score = int(input("정수를 입력하세요: "))

def get_grade(score):
    if score == 100:
        grade = "S"
    elif score >= 90:
        grade = "A"
    elif score >= 80:
        grade = "B"
    elif score >= 70:
        grade = "C"
    elif score >= 60:
        grade = "D"
    else:
        grade = "F"
    return grade

grade = get_grade(score)
print(f"학생번호: {student_id}, 점수: {score}, 학점: {grade}")
