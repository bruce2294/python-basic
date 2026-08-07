role = """
정수하나를 매개변수로 전달받아 정수값의 2배를 구해서
리턴하는 함수를 만들고 사용해 보세요.
"""
print(role)
def get_double(num):
    return num * 2

get_twice = lambda x: x * 2

print(get_double(5))
print(get_twice(5))

role = """
가로, 세로 길이를 매개변수로 전달받아 삼각형의 넓이를 구해서
리턴하는 함수를 만들고 사용해 보세요.
"""
print(role)
get_triangle_area = lambda x, y: int((x * y) / 2)
print(get_triangle_area(3, 4))

role = """
가로, 세로 길이를 매개변수로 전달받아 해당 길이로 사각형 그리는 함수 만들고 사용하기
w 와 h 매개변수 값이 전달되지 않으면 기본값(100, 100)으로 설정됨.
함수에 값을 보내면 무조건 앞에 매개변수부터 채워진다. w = 700
매개변수이름을 통해서 원하는 매개변수로 값을 전달할 수 있다.
"""
def rect(w=100, h=100):
    print("-" * 86)
    print("===> 사각형 그리기")
    print(f"가로길이: {w}, 세로길이: {h} 인 사각형을 그렸어요...")

rect(10, 20)
rect()
rect(700) # 함수에 값을 보내면 무조건 앞에 매개변수부터 채워진다. w = 700
rect(h = 700) # 매개변수이름을 통해서 원하는 매개변수로 값을 전달할 수 있다.
rect(h = 300, w = 200)
