"""
Перегрузка операторов сравнения

class Airplane:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def __str__(self):
        return "({0},{1})".format(self.x, self.y)

    def __lt__(self, other):
        self_mag = (self.x ** 2) + (self.y ** 2)
        other_mag = (other.x ** 2) + (other.y ** 2)
        return self_mag < other_mag

# задаем значения точек p1, p2, p3
p1 = Airplane(1,1)
p2 = Airplane(-2,-3)
p3 = Airplane(1,-1)

# используем «меньше чем»
print(p1<p2)
print(p2<p3)
print(p1<p3)"""

class Point:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def __str__(self):
        return "({0},{1})".format(self.x, self.y)

    def __add__(self, other):
        x = self.x + other.x
        y = self.y + other.y
        return Point(x, y)

# задаем координаты точек p1, p2
p1 = Point(1, 2)
p2 = Point(2, 3)

print(p1+p2)
