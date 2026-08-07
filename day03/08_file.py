from utils import print_line

# f = open("./test/test.log", "w", encoding="utf-8")
# f.write("안녕하세요\n")
# f.write("파이썬 파일 입출력입니다.")
# f.close()

f = open("./test/test.log", "r", encoding="utf-8")
content = f.read()
print(content)
f.close()

print_line()

with open("./test/test.log", "r", encoding="utf-8") as f:
    content = f.read()
    print(content)

print_line()
