# 이름과 나이를 입력받아서 나이가 18세이상이면
# xxx님은 성인이군요!
# 18세 미만이면
# xxx님은 미성년자군요!    ==> 출력되도록 해보세요
name = input("이름을 입력하세요: ")
age = int(input("나이를 입력하세요: "))

minor = "미성년자" if age < 18 else "성인"

print(f"{name}님은 {minor}이군요!")
