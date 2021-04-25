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
        self.x += dx # self.x = self.x + dx
        self.y += dy

    @property
    def x(self):
        return self.__x # тук трябва да остане __x 

    @x.setter
    def x(self, x):
        assert type(x) is int and x >= 0, 'x must be positive number'
        self.__x = x
    
    @property
    def y(self):
        return self.__y 

    @y.setter
    def y(self, y):
        assert type(y) is int and y >= 0, 'y must be positive number'
        self.__y = y

if __name__ == '__main__':

    # 2. променлива от типа Point
    # клас - типа, Point , обект - представител на класа p
    p1 = Point(20, 30)
    p2 = Point(15, 35)

    print(f'getters: ({p1.x}, {p1.y})')
    p1.x = 10
    p1.y = 20
    p1.draw()
    p1.move_to(6, 90)
    p1.draw()

    

    print('---')