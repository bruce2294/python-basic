print("""
학생번호, 이름을 생성자로 멤버변수에 초기화하고
학생정보를 출력하는 메소드를 가는 클래스 만들기
""")
class Student:
    def __init__(self, student_id, name):
        self.student_id = student_id
        self.name = name

    def show_info(self):
        print(f"학생번호: {self.student_id}, 이름: {self.name}")

s1 = Student(student_id="s01", name="철수")
s1.show_info()
print("-" * 86)

print("""
도서정보(도서제목, 가격, 출판사) 에 대한 정보를 멤버변수로 갖는 클래스를 만들고
도서정보를 클릭하는 메서드 / 10% 할인된 가격정보를 갖는 메서드를 가각 만들고 호출해서 사용해 보세요

[출력예시]
=== [도서 정보] ===
도서제목: 파이썬 기초 문법
기존가격: 20,000
출판사: 이지스퍼블리싱

=== [할인 정보] ===
10% 할인 가격: 18,000
""")
class Book:
    def __init__(self, title, price, publisher):
        self.title = title
        self.price = price
        self.publisher = publisher

    def show_info(self):
        print("=== [도서 정보] ===")
        print(f"도서제목: {self.title}")
        print(f"기존가격: {self.price:,}")
        print(f"출판사: {self.publisher}")

    def show_discount_price(self):
        print("=== [할인 정보] ===")
        print(f"10% 할인 가격: {int(self.price * (1 - 0.1)):,}")

b1 = Book(
    title="파이썬 기초 문법", 
    price=20000, 
    publisher="이지스퍼블리싱"
)
b1.show_info()
b1.show_discount_price()
print("-" * 86)
print(f"도서제목: {b1.title}")

b2 = Book(
    title = "MySQL의 정석",
    price = 20000,
    publisher = "한빛출판사"
)
b2.show_info()
b2.show_discount_price()
print(f"도서이름: {b2.title}")
