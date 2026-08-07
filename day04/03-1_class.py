role = """
### 기본 문법
class 클래스이름:
    def __init__(self, 매개변수):
        self.속성 = 매개변수

    def 메서드이름(self):
        실행할 코드
"""
print(role)

print("===> 예시 1 - 가장 간단한 클래스")
class Dog:
    def bark(self):
        print("멍멍!")

my_dog = Dog()
my_dog.bark()

print("===> 예시 2 - 생성자(__init__)로 속성 저장하기")
class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def bark(self):
        print(f"{self.age}세 {self.name}가 멍멍 짖습니다!")

my_dog = Dog(name="바둑이", age=3)
print(f"이름: {my_dog.name}")
print(f"나이: {my_dog.age}세")
my_dog.bark()

print("===> 예시 3 - 여러 개의 객체 만들기")
dog1 = Dog("바둑이", 3)
dog2 = Dog("초코", 5)
dog1.bark()
dog2.bark()

print("===> 예시 4 - 정보를 출력하는 메서드 만들기")
class Student:
    def __init__(self, name, student_id, major):
        self.name = name
        self.student_id = student_id
        self.major = major

    def show_info(self):
        print(f"이름: {self.name}, 학번: {self.student_id}, 학과: {self.major}")

s1 = Student(name="김철수", student_id="20240101", major="컴퓨터공학과")
s1.show_info()

print("===> 예시 5 - 메서드 안에서 다른 메서드 호출하기")
class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    def show(self):
        print(f"가로: {self.width}, 세로: {self.height}, 넓이: {self.area()}")

r = Rectangle(width=4, height=5)
r.show()
print("-" * 86)
role = """
## 3. 클래스 변수와 인스턴스 변수
### 인스턴스 변수 (Instance Variable)
`self.변수`로 선언하며, **객체마다 독립적으로** 값을 가집니다.

### 클래스 변수 (Class Variable)
클래스 내부, 메서드 밖에 선언하며, **해당 클래스로 만든 모든 객체가 공유**합니다.
"""
print(role)
class Student:
    school = "대구초등학교"

    def __init__(self, name):
        self.name = name

s1 = Student("철수")
s2 = Student("영희")

print(s1.school, s2.school)
Student.school = "경북고등학교"
print(s1.school, s2.school)

role = """
## 4. 상속 (Inheritance)

기존 클래스(부모 클래스)의 속성과 메서드를 물려받아 
새로운 클래스(자식 클래스)를 만드는 기능입니다. 
중복 코드를 줄이고 기능을 확장할 수 있습니다.

### 기본 문법

python

```python
class 자식클래스(부모클래스):
    ...
```
"""
print(role)
class Animal:
    name = "동물"

    def sound(self):
        print(f"{self.name}이 소리를 냅니다.")

class Dog(Animal):
    def __init__(self, my_name, breed):
        self.my_name = my_name
        self.breed = breed

    def sound(self):
        print(f"[{super().name}] {self.my_name}({self.breed})가 멍멍 짖습니다.)")

d = Dog("바둑이", "진돗개")
d.sound()

class Student:
    school = "대구고등학교" # 클래스 변수(모든 학생이 공유)
    def __init__(self, name):
        self.name = name # 인스턴스 변수(학생마다 다름)

s1 = Student("철수")
s2 = Student("영희")

print(s1.school, s2.school, sep=", ")
print(s1.name, s2.name, sep=", ")

Student.school = "경북고등학교" # 클래스 변수를 바꾸면
print(s1.school, s2.school, sep=", ") # 경북고등학교 경북고등학교(모두에게 반영됨)
