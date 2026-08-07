# 이름, 국어, 영어 점수 입력받아 이름과 총점을 구해서 출력하기
name = input("이름을 입력하세요: ")
kor = int(input("국어 점수를 입력하세요: "))
eng = int(input("영어 점수를 입력하세요: "))
avg = (kor + eng) / 2
print(f"평균 : {avg:.0f}")

result = "합격" if avg >= 80 else "불합격"
print(f"{name}님은 {result}입니다.")
