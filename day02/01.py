fruits = ["사과", "포도", "바나나", "수박"]
# for a in fruits:
#     print(a)

for index, fruit in enumerate(fruits, start = 1):
    # print(index, fruit)
    print(f"{index} -> {fruit}")

# for i in range(1, 10):
#     if i == 5:
#         break
#     print(i)

# for i in range(1, 6):
#     if i == 3:
#         continue
#     print(i)

# for i in range(0, 3): #0, 1, 2 세번 루프를 돈다.
#     input_user_id = input("아이디입력: ")
#     input_user_pwd = input("비밀번호입력: ")
#     if input_user_id == "hello" and input_user_pwd == "1234":
#         print("login success!")
#         break
#     else:
#         print("login fail~!")

# print("===> break")
# for _ in range(3):
#     user_id = input("id: ")
#     user_pwd = input("pwd: ")
#     # print(_)
#     if user_id == "admin" and user_pwd == "1234":
#         print("login success!")
#         break
#     else:
#         print("login fail~!!")

print("===> continue")
scores = [100, 40, 50, 90, 80]
for index, score in enumerate(scores):
    print(score)

role = "리스트에 저장된 정수의 총합을 구해서 출력"
print(role)
total = 0
for s in scores:
    total += s
print(f"total: {total}")

print(f"sum(scores): {sum(scores)}")

for i in range(2, 4):
    # print(f"i = {i}")
    for j in range(1, 4):
        # print(f"j = {j}")
        print(f"{i} x {j} = {i * j}")
