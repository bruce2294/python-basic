text = "PYTHON"
print("===> 인덱스로 한 글자만 가져오기")
print(text[0])
print(text[1])
print(text[2])
print(", ".join(one_char for one_char in text))

role = """
===> 슬라이싱 기본 구문
문자열[시작인덱스:끝인덱스]
"""
print(role)

role = """
===> ===> 핵심 규칙 (가장 헷갈리는 부분!)
⚠️ "끝인덱스"는 포함되지 않습니다. 끝인덱스 "직전"까지만 잘라냅니다.
"""
print(role)
print(", ".join(str((index, c)) for index, c in enumerate(text[:3])))

role = """
### 시작인덱스, 끝인덱스 생략하기
- **시작인덱스 생략** → 처음부터
- **끝인덱스 생략** → 끝까지
"""
print(role)
print(text[:3])     # PYT   (처음부터 인덱스 2까지)
print(text[3:])     # HON   (인덱스 3부터 끝까지)
print(text[:])      # PYTHON (전체, 그대로 복사)

role = """
4. 슬라이싱 예시 5가지
"""
print(role)
example_1 = """
예시 1: 앞부분 잘라내기
name = "홍길동입니다"
print(name[0:3])    # 홍길동
print(name[:3]) 
"""
name = "홍길동입니다"
print(name[0:3])
print(name[:3])

example_1 = """
예시 5: 전화번호 뒷자리 마스킹 활용
phone = "010-1234-5678"
masked = phone[:9] + "****"
print(masked)    # 010-1234-****
"""
phone = "010-1234-5678"
masked = phone[:-4] + "****"
print(f"masked phone: {masked}")

role = """
5. 슬라이싱 응용: step(증가 폭) 활용
슬라이싱은 시작과 끝뿐만 아니라, 몇 칸씩 건너뛸지도 지정할 수 있습니다.
문자열[시작인덱스:끝인덱스:step]
"""
print(role)
example_1 = """
예시 1: 한 글자씩 건너뛰기
text = "PYTHON"
print(text[::2])    # PTO  (인덱스 0,2,4 글자만)
"""
print(example_1)
text = "PYTHON"
print(text[::2])

example_2 = """
예시 2: 문자열 뒤집기 (자주 쓰이는 활용법)
text = "PYTHON"
print(text[::-1])   # NOHTYP  (step을 -1로 주면 역순으로 출력)
"""
print(example_2)
text = "PYTHON"
print(text[::-1])
