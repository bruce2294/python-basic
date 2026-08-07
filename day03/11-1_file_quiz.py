quiz_1 = """
1. 학생이름과 연락처를 입력받아 student.txt파일에 저장하기
== 파일에 저장된 내용 예시 ===
홍길동,010-111-1234
이영희,010-4445555
김사랑,010-333-1233
"""
print(quiz_1)
with open("test/student.txt", "w", encoding="utf-8") as f:
    lines = []
    count = 0
    while True:
        name = input("학생이름(그만 입력 시 종료): ")
        if count > 100:
            print("최대 100 라인만 입력 가능합니다.")
        elif name == "그만":
            break

        phone = input("연락처: ")
        lines.append(f"{name},{phone}\n")
        count += 1
    f.writelines(lines)

quiz_2 = """
2. student.txt파일에 저장된 내용 읽어오기
"""
print(quiz_2)
with open("test/student.txt", "r", encoding="utf-8") as f:
    for line in f:
        print(line.strip)
