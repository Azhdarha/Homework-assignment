class Complex:
    def __init__(self, x, y): # конструктор класса
        self.x = x
        self.y = y
    def setX(self, x):
        self.x = x
    def __str__(self): # преобразование объекта в строку
        return '(' + str(self.x) + ', ' + str(self.y) + ')'
    def __eq__(self, other): # перегружен "=="
        if self.x == other.x and self.y == other.y: return True
        return False
    def __add__(self, other): # перегружен "+"
        return Complex(self.x + other.x, self.y + other.y)
    def __hash__(self):
        return 17*self.x + self.y
 
a = Complex(1,2)
b = Complex(3,1)
c = a + b
print(a is b)
print(a == b)
print(c)