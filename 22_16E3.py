class Circle:
    circle = "круг"
class Square(Circle):
    square = "квадрат"
inscribed = Square()
print(inscribed.circle + "в нем" + str(inscribed.square))