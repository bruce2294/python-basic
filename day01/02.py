name = input("이름을 입력하세요: ")
age = int(input("나이를 입력하세요: "))
print(f"안녕하세요, {name}님! 나이는 {age}살 이시군요.")

age_str = input("나이 String을 입력하세요: ")
print(f"나이 String 곱하기 3은 {(age_str * 3)}살 이시군요.")

type_of_name = type(name)
type_of_age = type(age)
type_of_age_str = type(age_str)
print(f"입력한 이름의 타입은 {type_of_name}입니다.")
print(f"입력한 나이의 타입은 {type_of_age}입니다.")
print(f"입력한 나이 String의 타입은 {type_of_age_str}입니다.")
