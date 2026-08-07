class Rect:
    def draw_rect(self):
        print("사각형을 그려요")
    def draw_paint(self):
        print("사각형을 칠해요")

class Circle:
    def draw_circle(self):
        print("타원을 그려요")
    def circle_paint(self):
        print("타원을 칠해요")

a = Rect()
a.draw_rect()
a.draw_paint()

b = Rect()
b.draw_rect()
b.draw_paint()

c = Circle()
c.draw_circle()
c.circle_paint()
