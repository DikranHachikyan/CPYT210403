# 1. дефиниция на класа

class Point():
    
    def __init__(self, x = 0, y = 0, *args, **kwargs):
        print('object ctor')
        # данни на класа
        self.__x = x
        self.__y = y

    # Методи
    def draw(self):
        print(f'draw point at ({self.__x}, {self.__y})')

    def move_to(self, dx, dy):
        self.__x += dx
        self.__y += dy

    def set_x(self, x):
        assert type(x) is int and x >= 0 , 'x must be positive number'
        self.__x = x

    def get_x(self):
        return self.__x

if __name__ == '__main__':

    # 2. променлива от типа Point
    # клас - типа, Point , обект - представител на класа p
    p1 = Point(20,30)
    p2 = Point(15, 35)

    # print(f'direct access: ({p1.__x}, {p1.__y})')
    p1.set_x('10')
    p1.draw()
    p1.move_to(6, 9)
    p1.draw()

    

    print('---')