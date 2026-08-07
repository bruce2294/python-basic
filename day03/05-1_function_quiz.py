quiz_1 = """
1. 아래와 같은 리스트를 모두 출력해 보세요 
animals = ["cat", "dog", "rabbit"]
동물이름을 입력받아 리스트에 추가해 보세요
"""
print(quiz_1)
def append_animal(animals = [], input_animal = ""):
    if input_animal in animals:
        return False
    animals.append(input_animal)
    return True

animals = ["cat", "dog", "rabbit"]
input_animal = input("동물이름을 입력하세요: ")
appended = append_animal(animals, input_animal)
result = input_animal + ' 를/을 animals 에 추가하였습니다.' if appended else input_animal + ' 는/은 이미 animals 에 있습니다.'

print(result)
print(f"animals: {animals}")

quiz_2 = """
2. 회원이름을 튜플에 저장하고 전체 데이터를 출력해 보세요.
"""
print(quiz_2)
members = ("영수", "영호", "영식", "영철", "광수")
print("\n".join(f"{index}: {member}" for index, member in enumerate(members, start=1)))

quit_3 = """
3. 이름이 "철수"이고 나이가 20인 딕셔너리를 만들고 출력해 보세요
   딕셔너리에 "연락처"가 "010-111-1234"인 데이터를 key와 value로 추가해보세요
   딕셔너리에 저장된 정보들을 출력해 보세요
"""
print(quit_3)
def print_student_info(student={}):
    for key, value in student.items():
        print(f"{key}: {value}")

student = {"name": "철수", "age": 20}
print_student_info(student)
print("===> add student phone")
student["phone"] = "010-111-1234"
print_student_info(student)

quiz_4 = """
4. 두 정수를 매개변수로 전달받아 두 수를 곱해서 반환하는 함수를 만들고 호출해서 사용해 보세요.
"""
print(quiz_4)
def multiply_numbers(*args):
    result = 1
    for arg in args:
        result *= arg
    return result

a, b = 10, 20
print(f"{a} * {b} = {multiply_numbers(a, b)}")
