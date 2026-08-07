import csv
import os

# test 폴더가 없으면 생성
os.makedirs("./test", exist_ok=True)

with open("./test/student.csv", "w", newline="", encoding="utf-8") as f:
    writer = csv.writer(f)
    writer.writerow(["이름", "나이", "성적"])
    writer.writerow(["철수", 20, 85])
    writer.writerow(["영희", 22, 92])
print("csv파일로 저장완료!")

with open("./test/student.csv", "r", encoding="utf-8") as f:
    reader = csv.reader(f)
    for row in reader:
        print(row)
# ['이름', '나이', '성적']
# ['철수', '20', '85']
# ['영희', '22', '92']
print("csv파일에 있는 숫자도 문자처리됨")
