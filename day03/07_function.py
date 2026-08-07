role = """
가변 인자
*args -> 전달되 매개변수값들을 args 라는 튜플로 받는다.
"""
print(role)
def total_sum(*args):
    print(f"args: {args}, type: {type(args)}")
    return sum(args)

print(total_sum(1, 2))
print(total_sum(1, 2, 3))

print("-" * 80)
total_sum_lambda = lambda *args: sum(args)
print(total_sum_lambda(1, 2))
print(total_sum_lambda(1, 2, 3))

print("-" * 80)
print("*args -> 전달되 매개변수값들을 args 라는 튜플로 받는다.")
def tuple_total_sum(args=()):
    return sum(args)
print(tuple_total_sum((1, 2, 3)))

print("-" * 80)
role = """
10 + "명" 은 안됨
"""
# print(10 + "명")
print(str(10) + "명")

role = """
### 3-4. 가변 키워드 인자 `**kwargs`
이름이 정해지지 않은 여러 개의 키워드 인자를 딕셔너리 형태로 받습니다.
"""
print(role)
def print_info(**kwargs):
    print(f"kwargs: {kwargs}, type: {type(kwargs)}")
    # 언패킹
    for key, value in kwargs.items():
        print(f"{key}: {value}")

print_info(name = "민수", age = 30, job = "개발자")

role = """
### 3-5. 모두 함께 사용하기
"""
print(role)
def example(a, b, *args, c=10, **kwargs):
    print(a, b, args, c, kwargs)
example(1, 2, 3, 4, c = 100, d = 5, e = 6)
# example(a = 1, b = 2, 3, 4, c = 100, d = 5, e = 6) # 에러
example(1, 2, 3, 4, c = 100, d = 5, e = 6) # 에러

role = """
함수안에 전역변수 사용하기
"""
print(role)
count = 0
def increase_wrong():
    count += 1 # UnboundLocalError 에러까지: count 라는 변수를 선언하지 않아서
increase_wrong()
print(count)

def increase():
    global count
    count += 1
increase()
print(count)
