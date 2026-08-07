role = """
리스트 컴프리헨션 (한 줄로 리스트 만들기, 참고용)
squares = [n * n for n in range(1, 6)]
"""
print(role)
squares = [n * n for n in range(1, 6)]
print(squares)

tuple_1 = ("영수", "영호", "영식", "영철", "광수")
print(", ".join(name for name in tuple_1))

role = """
튜플로 선언하기
"""
print(role)
colors = ("빨강", "파랑", "초록")
print(colors[0])
print(colors[-1])
print(colors[:2])
print(colors[-2:])
# colors[0] = "RED" # TypeError: 'tuple' object does not support item assignment

person = ("홍길동", 20, "컴퓨터공학과")
print(", ".join(str(info) for info in person))

name = person[0]
age = person[1]
department = person[2]
print(name, age, department, end=", ")

print() #줄바꿈
role = """
===> 언패킹
person = ("홍길동", 20, "컴퓨터공학과")
name, age, department = person
"""
print(role)
name, age, department = person
print(name, age, department, end=", ")
print() #줄바꿈

role = """
변수값 교환(swap)에 활요
"""
print(role)
a = 1
b = 2
a, b = b, a
print(a, b)

role = """
원소가 1개인 튜플 주의사항
not_tuple = (1)
real_tuple = (1, )
"""
print(role)
print(type((1)))
print(type((1, )))

print("===> 딕셔너리(Dictionary) - 키: 밸류, 라벨링")
student = {"name": "홍길동", "age": 20, "major": "컴퓨터공학과"}
print(student)
print(type(student))

print(student["name"])
# a = student["phone"] # 키값이 없으면 오류!
print(f"{student.get("phone")}, get 함수로 하면 딕셔너리 에 키값 없어도 에러안남")
print(student.keys())
print(type(student.keys()))
print(", ".join(key for key in student.keys()))

role = """
학생번호 이름 국어 영어점수를 딕셔너리에 저장하고 전체 정보를 출력해 보세요
"""
print(role)
student = {"student_id": "s01", "name": "홍길동", "grade": 5, "kor_score": 90, "eng_score": 80}
print(student)
del student["grade"]
print(f"grade삭제후 -> {student}")
student_score = []
for key in student.keys():
    student_score.append(student[key])

print(", ".join(str(student[key]) for key in student.keys()))
print(student_score)

dict_student_score = student.values()
print(dict_student_score)
print(type(dict_student_score))

tuple_student_score = tuple(student.values())
print(tuple_student_score)
print(type(tuple_student_score))

items_student_score = student.items()
print(items_student_score)
print(type(items_student_score))

for item in items_student_score:
    print(f"item: {item}, type: {type(item)}")
