class Box:
    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y

    def getArea(self):
        return self.x * self.y
    
    def printArea(self):
        print(f"가로: {self.x}, 세로: {self.y}, 사각형 넓이: {self.x * self.y}")

b1 = Box(x=10, y=20)
b1.printArea()

print("""
위의 클래스(Box)를 상속받아 삼각형의 넓이를 구하는 클래스를 만들어보세요.
(*printArea 메서드를 오버라이딩 해서 삼각형 넓이 구하기)
""")

class Triangle(Box):
    def __init__(self, x, y):
        super().__init__(x, y)

    def getArea(self):
        return super().getArea() / 2

    def printArea(self):
        print(f"가로: {self.x}, 세로: {self.y}, 삼각형 넓이: {self.getArea()}")

x, y = 5, 6
t1 = Triangle(x=x, y=y)
print(f"가로: {x}, 세로: {y}, 삼각형 넓이: {t1.getArea()}")
t1.printArea()
