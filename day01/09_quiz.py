role = """
===> 번호, 국어점수, 영어점수를 입력받아 평균이 70이상이면 합격 아니면 불합격 출력
     단 국어점수 또는 영어점수가 60점 미만이면 불합격
"""
print(role)
student_id = input("학생번호를 입력하세요: ")
kor = int(input("국어점수를 입력하세요: "))
eng = int(input("영어점수를 입력하세요: "))
def get_fail(score):
    return "과락" if score < 60 else "PASS"

def get_pass_fail(kor, eng):
    avg = (kor + eng) / 2
    if kor < 60 or eng < 60:
        result = "불합격"
    elif avg >= 70:
        result = "합격"
    else:
        result = "불합격"
    return result

pass_fail_result = get_pass_fail(kor, eng)
kor_fail = get_fail(kor)
eng_fail = get_fail(eng)
result = f"""
학생번호: {student_id},
국어점수: {kor} -> {kor_fail},
영어점수: {eng} -> {eng_fail},
결과: {pass_fail_result}
"""
print(result)
