from utils import print_line, file_end, print_decorated_title

f = open("greeting.txt", "w", encoding="utf-8")
f.write("안녕하세요~\n")
f.write("파이썬 파일 입출력입니다.")
file_end(f)
print(f"-> f.closed(): {f.closed}")
f.close()
print(f"-> f.closed(): {f.closed}")

print_line()
f = open("greeting.txt", "r", encoding="utf-8")
content = f.read()
print(content)
f.close()

print_line()
with open("greeting.txt", "a", encoding="utf-8") as f:
    f.write("Hello World~!")
    file_end(f)

with open("greeting.txt", "r", encoding="utf-8") as f:
    content = f.read()
    print(content)

print_line()
with open("greeting.txt", "r", encoding="utf-8") as f:
    lines = f.readlines()
    print(f"{lines}")

    for index, line in enumerate(f):
        print(f"{index}: {line}")

print_line()
with open("greeting.txt", "r", encoding="utf-8") as f:
    for index, line in enumerate(f):
        # print(f"{index}: {line.removesuffix("\n")}")
        print(f"{index}: {line.strip()}") # data 문자뒤의 불필요한 문자 - \n  제거한다.

print_line()
role = """
노랫가사를 입력받아서 mysong.txt 파일로 저장(종료조건 => exit 입력)
"""
print(role)
with open("mysong.txt", "w", encoding="utf-8") as f:
    while True:
        line = input("노랫가사 입력: ")
        if line == 'exit':
            break
        f.write(line+"\n")
print("노랫가사가 저장되었어요..")
print_line()
print_decorated_title("저장된 노랫가사 화면에 출력하기")
with open("mysong.txt", "r", encoding="utf-8") as f:
    for index, line in enumerate(f, start=1):
        print(f"{index} {line.strip()}")
print_line()
