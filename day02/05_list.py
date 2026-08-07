import pandas as pd
role = """
학생점수를 입력받아 리스트에 저장하고(append함수)
전체총점/전체평균/최대점수/최소점수 구하기
"""
scores = []
while True:
    score = int(input("학생점수입력(종료 -> -1 입력): "))
    if score == -1:
        print("입력 종료 => scores: ", scores)
        break
    scores.append(score)

print("전체총점 -> sum(scores): ", sum(scores))
print("전체평균 -> sum(scores) / len(scores): ", round((sum(scores) / len(scores)), 2))
print("전체평균 from pandas -> pd.DataFrame(scores).mean(): ", pd.DataFrame(scores).mean().round(2))
print("최대점수 -> max(scores): ", max(scores))
print("최소점수 -> min(scores): ", min(scores))

sorted_scores = sorted(scores)
print(f"sorted(scores): {sorted_scores}")
sorted_scores = sorted(scores, reverse=1)
print(f"sorted(scores, reverse=1): {sorted_scores}")

role = """
학생이름을 3명 입력받아서 list에 저장하고(exit 입력할때까지 입력받아 저장해도 됨.)
전체 저장된 학생 이름들을 출력해 보세요.
출력은 이름순으로(오름차순정렬) 출력하세요.
"""
students = []
while True:
    student = input("학생이름을 입력하세요(종료 -> exit 입력): ")
    if student == "exit":
        print(f"입력완료, students: {students}")
        break
    students.append(student)
print(f"sorted students: {sorted(students, reverse=0)}")
