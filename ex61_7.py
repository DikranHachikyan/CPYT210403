# 1. дефиниция на класа

class Point():
    
    def __init__(self):
        print('object ctor')
        # данни на класа
        self.x = 10
        self.y = 20

    # Методи
    def draw(self):
        print(f'draw point at ({self.x}, {self.y})')

if __name__ == '__main__':

    # 2. променлива от типа Point
    # клас - типа, Point , обект - представител на класа p
    p = Point()

    print(f'Point ({p.x}, {p.y})')
    p.draw()

    print('---')