quiz_1 = """
1. 학생이름과 연락처를 입력받아 student.txt파일에 저장하기
== 파일에 저장된 내용 예시 ===
홍길동,010-111-1234
이영희,010-4445555
김사랑,010-333-1233
"""
print(quiz_1)
with open("student.txt", "w", encoding="utf-8") as f:
    while True:
        name = input("이름(그만 입력 시 종료): ")
        if name == "그만":
            break
        phone = input("연락처: ")
        if phone == "그만":
            break
        f.write(f"{name},{phone}\n")

quiz_2 = """
2. student.txt파일에 저장된 내용 읽어오기
"""
print(quiz_2)
def mask_info(text="", unit=1):
    return text[:-unit] + ("*" * unit)

with open("student.txt", "r", encoding="utf-8") as f:
    option = input("개인정보 보호 여부(y/n): ")
    for index, line in enumerate(f, start=1):
        if option == "n":
            print(f"{index} {line.strip()}")
        else:
            name, phone = line.strip().split(",")
            print(f"{index} {mask_info(name, 1)},{mask_info(phone, 4)}")
