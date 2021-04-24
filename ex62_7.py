# 1. дефиниция на класа

class Point():
    
    def __init__(self, x = 0, y = 0, *args, **kwargs):
        print('object ctor')
        # данни на класа
        self.x = x
        self.y = y

    # Методи
    def draw(self):
        print(f'draw point at ({self.x}, {self.y})')

    def move_to(self, dx, dy):
        self.x += dx
        self.y += dy

if __name__ == '__main__':

    # 2. променлива от типа Point
    # клас - типа, Point , обект - представител на класа p
    p1 = Point()
    p2 = Point(15, 35)

    print(f'Point ({p1.x}, {p1.y})')
    p1.draw()

    p2.draw()
    p2.move_to(30, -5)
    p2.draw()

    print('---')