role = """
===> 1. 자신의 이름, 나이, 연락처를 입력받아 출력해 보세요
"""
print(role)
name = input("이름을 입력하세요: ")
age = int(input("나이를 입력하세요: "))
phone = input("연락처를 입력하세요: ")

print(f"이름: {name}, 나이: {age}, 연락처: {phone}")

role = """
===> 1-1. 여러줄로 표시하고 싶어요.
"""
print(role)
info = f"""
이름: {name},
나이: {age},
연락처: {phone}
"""
print(info)

role = """ ===> 아이디와 비밀번호를 입력받아 로그인처리
"""
print(role)

user_id = input("아이디를 입력하세요: ")
user_pw = input("비밀번호를 입력하세요: ")
def check_login(uid, pw):
    return "로그인 성공!!!!" if uid == "admin" and pw == "1234" else "로그인 실패!!!!"

login_result = check_login(user_id, user_pw)

print(f"로그인 결과: {login_result}")

"""
def check_admin_login(uid, pw):
    return "관리자 로그인 성공!!!!" if uid == "admin" and pw == "1234" else "일반회원 로그인 성공!!!!" if uid == "python" and pw == "5678" else "로그인 실패!!!!"
"""
def check_admin_login(uid, pw):
    if uid == "admin" and pw == "1234":
        return "관리자 로그인 성공!!!!"
    elif uid == "python" and pw == "5678":
        return "일반회원 로그인 성공!!!!"
    else:
        return "로그인 실패!!!!"

admin_login_result = check_admin_login(user_id, user_pw)
print(f"로그인 결과: {admin_login_result}")

role = """
===> 로그인 성공 시, 관리자/일반회원 구분해서 출력
print(role)
"""
def check_admin(user_id):
    return "일반회원" if not user_id == "admin" else "관리자"

print(f"로그인 결과: {check_login(user_id, user_pw)}, 회원구분: {check_admin(user_id)}")
