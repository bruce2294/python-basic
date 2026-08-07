scores = [1, 2, 3, 4, 5, 6, 7]
for index, score in enumerate(scores):
    print(f"[{index}]: {score}", end=", ")
print()

print(f"scores[1:4]: {scores[1:4]}")
print(f"scores[:-1: {scores[:-1]}")
print(f"scores[1:6]: {scores[1:6]}")
print(f"scores[1:-1]: {scores[1:-1]}")
print(f"scores[1:]: {scores[1:]}")
print(f"scores[:5]: {scores[:5]}")
print(f"scores[:50]: {scores[:50]}")
print(f"scores[-80:]: {scores[-80:]}")

stu_info = ["홍길동", "1234", [1, 2, 3]]
print(stu_info)
print(stu_info[0])
print(stu_info[1])
print(stu_info[2])

print(stu_info[2][0], stu_info[2][1], stu_info[2][2])
print(stu_info[0][0])
