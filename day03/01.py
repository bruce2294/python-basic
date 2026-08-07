role = """
1부터 100까지 수를 for를 이용해서 출력해 보세요.
"""
print(role)
# for num in range(1, 101):
#     print(num, end=", ")
print(", ".join(str(num) for num in range(1, 101)))

role = """
for 문으로 리스트의 모든 요소를 출력해 보세요
"""
names = ["한나라", "이나라", "삼나라", "이철수"]
print(", ".join(name for name in names))

role = """
while 문을 1 ~ 10 출력하기
"""
print(role)
num_list = list(range(1, 11))
while num_list:
    print(num_list.pop(0), end=", ")

range_list = range(1, 11)
print(type(range_list))

role = """
break, continue
"""
print(role)
