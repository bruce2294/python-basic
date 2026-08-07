role = """
학생이름, 연락처 입력받아 파일로 저장하기
"""
with open("student.txt", "w", encoding="utf-8") as f:
    name = input("학생이름: ")
    phone = input("연락처: ")
    f.write(f"{name},{phone}\n")
print("입력된 정보가 파일로 저장되었어요~")

with open("student.txt", "a", encoding="utf-8") as f:
    name = input("학생이름: ")
    phone = input("연락처: ")
    f.write(f"{name},{phone}\n")
print("입력된 정보가 파일에 추가되었어요~")
