"""
if문 / for문 퀴즈
### 문제 1
사용자로부터 숫자를 입력받아 3의 배수이면서 5의 배수이면 `15의 배수`, 그렇지 않으면 `해당 없음`을 출력하세요.

### 문제 2
아이디와 비밀번호를 입력받아 로그인 여부를 출력하세요.

### 문제 3
상품 금액을 입력받아 할인율을 적용된 금액을 계산하세요.

단일 for문 퀴즈
### 문제 1
1부터 100까지 숫자 중에서 3의 배수만 출력하세요.

### 문제 2
1부터 100까지의 숫자 중 짝수의 합을 구하세요.

### 문제 3
리스트에 학생이름 5명을 저장하고 모든 학생이름을 출력해 보세요
"""

print("=====> if문 / for문 퀴즈")
quiz_1 = """
===> ### 문제 1
사용자로부터 숫자를 입력받아 3의 배수이면서 5의 배수이면 `15의 배수`, 그렇지 않으면 `해당 없음`을 출력하세요.
"""
input_num = int(input("숫자를 입력해주세요: "))
def check_multiple(num):
    return "15의 배수" if num % 3 ==0 and num % 5 == 0 else "해당 없음"
print(check_multiple(input_num))
print() #줄바꿈

quiz_2 = """
===> ### 문제 2
아이디와 비밀번호를 입력받아 로그인 여부를 출력하세요.
"""
input_user_id = input("아이디를 입력하세요: ")
input_user_pw = input("비밀번호를 입력하세요: ")
def check_login(user_id, user_pw):
    return "로그인 성공" if user_id == "python" and user_pw == "1234" else "로그인 실패"
print(check_login(input_user_id, input_user_pw))
print() #줄바꿈

quiz_3 = """
===> ### 문제 3
리스트에 학생이름 5명을 저장하고 모든 학생이름을 출력해 보세요
"""
student_names = ["영수", "영호", "영식", "영철", "광수"]
for name in student_names:
    print(name)
print() #줄바꿈
for name in student_names:
    print(name, end = ",")
print() #줄바꿈
print(", ".join(student_names))
print() #줄바꿈

print("=====> 단일 for문 퀴즈")
quiz_4 = """
===> ### 문제 4
1부터 100까지 숫자 중에서 3의 배수만 출력하세요.
"""
for n in range(1, 101):
    if n % 3 == 0:
        print(n, end = ", ")
print() #줄바꿈
nums = list(range(1, 101))
print(nums)
# print(", ".join(nums)) # 에러 해결해야 함.

quiz_5 = """
===>### 문제 5
1부터 100까지의 숫자 중 짝수의 합을 구하세요.
"""
print(quiz_5)
sum = 0
for n in range(1, 101):
    sum += n
print(f"sum : {sum}")

sum = 0
for n in range(1, 101):
    if n % 2 == 0:
        sum += n
print(f"sum : {sum}")

sum = 0
for n in range(1, 101):
    if not n % 2 == 0:
        sum += n
print(f"sum : {sum}")
print() #줄바꿈

quiz_6 = """
===>### 문제 6
리스트에 학생이름 5명을 저장하고 모든 학생이름을 출력해 보세요
"""
print(quiz_6)
student_names = ["영숙", "정숙", "영자", "순자", "옥순"]
for student_name in student_names:
    print(student_name)
print() #줄바꿈

quiz_x = """
**프롬프트**
나는 오늘 파이썬 연산자/if문/단일for문을 배웠어.
코드를 직접 작성해 볼수 있는 퀴즈를 내줘.

퀴즈 예시)
리스트에 학생이름 5명을 저장하고 모든 학생이름을 출력해 보세요.

실행결과:
영숙
정숙
영자
순자
옥순
"""
