fruits = ["사과", "바나나", "포도"]
print(fruits)
print(type(fruits))

print(fruits[0])
print(fruits[1])
print(fruits[-1])

print(fruits[1:])
print(fruits[:1])

print("append('수박') -> 수박추가")
fruits.append("수박")
print(fruits)
print("insert(1, '오렌지') -> 오렌지 삽입")
fruits.insert(1, "오렌지")
print(fruits)

print("fruits[2] = '딸기' -> 바나나 업데이트 to 딸기")
fruits[2] = "딸기"
print(fruits)

print("remove('수박') -> 수박제거")
fruits.remove("수박")
print(fruits)

while fruits:
    print(f"{fruits.pop(0)} 판매완료, 재고: {fruits}")
print(fruits)

quiz_1 = """
5명의 학생이름을 list에 저장해 보세요.
전체 학생이름을 출력해 보세요.(for문 사용)
전학온 학생이름 1명을 추가해 보세요.(맨 마지막에 추가해 보세요. append메소드)
0번째 위치 학생 이름을 수정해 보세요.
"""
print(quiz_1)
students = ["영수", "영호", "영식", "영철", "광수"]
for index, student in enumerate(students, start=1):
    print(f"{index}번: {student}")

print("학생추가")
students.append("상철")
print(students)

print("0번학생 수정")
students[0] = "경수"
print(students)

scores = [100, 50, 60, 80, 10, 90]
print(f"초기 리스트: {scores}")
print("append(70)")
scores.append(70)
print(scores)
print("remove(100)")
scores.remove(100)
print(scores)
# scores.remove(20) # 20의 값 삭제 => remove 함수는 값이 없으면 에러 발생
print("*" * 30)
scores = [100, 50, 60, 80, 10, 90]
print(f"리스트 초기화: {scores}")
print("pop() -> 마지막요소삭제")
a = scores.pop()
print(f"마지막요소삭제후 ==> {scores}")
print("삭제된 값=>", a)
print("del scores[0]")
del scores[0]
print(scores)
print("리스트합 => ", sum(scores))
print("최대값 => ", max(scores))
print("최소값 => ", min(scores))
print("갯수 => ", len(scores))
