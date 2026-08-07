class Animal:
    def __init__(self, name):
        self.name = name

    def sound(self):
        print(f"동물 {self.name}는 소리를 냅니다.")

    def eat(self):
        print(f"동물 {self.name}는 냠냠 먹습니다.")

a1 = Animal("원숭이")
a1.sound()
a1.eat()

print("-" * 86)

class Dog(Animal):
    def __init__(self, name: str, breed: tuple):
        super().__init__(name)
        self.breed = breed

    def sound(self): # 기능수정(오버라이딩)
        print(f"{self.name}({self.breed})가 멍멍 짖습니다.")

    def wag(self): #기능추가(메서드 추가)
        pass # 로직 추가하기 전에 함수만 선언, 아무의미 없음.
        pass  # TODO: 나중에 할인 로직 작성 예정
        print(f"{self.name}는 주인을 보고 꼬리를 흔들어요~")

d1 = Dog(
    name = "바둑이",
    breed = "진돗개"
)
d1.sound()
d1.eat()
d1.wag()

class Cat(Animal):
    def sound(self):
        print(f"{self.name}는 야웅야웅~~~")

    def catch_mouse(self):
        print(f"{self.name}는 캐치캐치~! 쥐를 잡아요~~~")

c1 = Cat("야웅이")
c1.sound()
c1.catch_mouse()

print("-" * 86)
class Swinmer:
    def __init__(self, age: int):
        self.age = age
        
    def swim(self):
        print(f"나이 {self.age}에 수영을 합니다.")

s1 = Swinmer(age=50)
s1.swim()

class MarineAnimals(Animal, Swinmer):
    def __init__(self, name: str, age: int):
        Animal.__init__(self, name=name)
        Swinmer.__init__(self, age=age)

m1 = MarineAnimals("멍멍이", 20)
m1.eat()
m1.swim()
