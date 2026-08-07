count = 0
while count < 5:
    print(count)
    count += 1
print(f"while after count: {count}")

number = 10
while number > 0:
    print(number)
    number -= 2
print(f"while after number: {number}")

tasks = ["청소", "빨래", "설거지"]
while tasks:
    task = tasks.pop(0)
    print(f"<{task}> 완료, 남은 일: {tasks}")
print(f"while after tasks: {tasks}")

# role = "1부터 100까지 출력하세요. 단 한줄에 10개씩 출력하세요. ==> while문 사용"
# print(role)
# list = list(range(1, 101))
# while list:
#     number = list.pop(0)
#     print(number, end=", ")
#     if number % 10 == 0:
#         print()

role = "1부터 100까지 출력하세요. 단 한줄에 10개씩 출력하세요. ==> for문 람다 사용"
print(role)
for i in range(11):
    print(f"{[j for j in range(11)]}")

role = """
단을 입력받아 구구단 출력해 보기
단입력: 3
3단
3 * 1 = 3
3 * 2 = 6
...
3 * 9 = 27
"""
# input = int(input("단입력: "))
# for i in range(1, 10):
#     print(f"{input} * {i} = {input * i}")

# for i in range(9):
#     for j in range(9):
#         if j <= i:
#             print("*", end = " ")
#     print()

# role = "단입력받아 구구단 출력하기 -> while문 사용해 보기"
# print(role)
# input = int(input("단입력: "))
# num_list = list(range(1, 10))
# while num_list:
#     num = num_list.pop(0)
#     print(f"{input} * {num} = {input * num}")

import getpass
role = "로그인정보 맞을 때 까지 무한 입력"
while True:
    user_id = input("id: ")
    user_pwd = getpass.getpass("pwd: ")
    # print(_)
    if user_id == "admin" and user_pwd == "1234":
        print("login success!")
        break
    else:
        print("login fail~!!")
