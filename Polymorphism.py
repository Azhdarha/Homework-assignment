class Rectangle():
    def __init__(self,str1,str2):
        self.str1=str1
        self.str2=str2
        self.prm=0
        self.ploshd=0
    def perimetr (self):
        self.prm=(self.str1+self.str2)*2
        return self.prm
    def area(self):
        self.ploshd=(self.str1*self.str2)
        return self.ploshd
    def info(self):
        p= self.perimetr()
        s= self.area()
        print(f" Периметр прямоугольника со сторонами {self.str1} cm и {self.str2} cm равен {p} cm, Площадь {s}")
      
fig1 = Rectangle (2, 4)
fig1.info()
print()
class Triangle():
    def __init__(self, a,b,c,h):
        self.b=b
        self.h=h
        self.a=a
        self.c=c
        self.prm=0
        self.ploshd=0
    def perimetr (self):
        self.prm=(self.a+self.b+self.c)
        return self.prm
    def area(self):
        self.ploshd=(self.b*self.h)/2
        return self.ploshd 
    def info(self):
        p= self.perimetr()
        s= self.area()
        print(f" Периметр треугольника со сторонами {self.a} cm и {self.b} cm и {self.c} пириметр = {p}, Площадь c высотой {self.h} Площадь {s}" )
fig1 = Triangle (2, 4, 5 , 6)
fig1.info()
print()
class Circle():
    def __init__(self, r):
        self.r=r
        self.prm=0
        self.ploshd=0
    def perimetr (self):
        self.prm=(2*3.14)*self.r
        return self.prm
    def area(self):
        self.ploshd=3.14*(self.r**2)
        return self.ploshd 
    def info(self):
        p= self.perimetr()
        s= self.area()
        print(f" Периметр круга с радиусом {self.r} пириметр = {p}, Площадь {s}" )
fig1 = Circle (6)
fig1.info()
print()