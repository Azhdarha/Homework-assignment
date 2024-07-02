"""
Используя механизм множественного наследования разработайте класс “Автомобиль”. 
Должны быть классы «Колеса», «Двигатель», «Двери».
"""

class Car:
    def __init__(self, Wheels, Engine, Doors):
        self.wheels = wheels
        self.engine = engine
        self.doors = doors

    def get_sound(self):
        return f"{self.__class__.__name__}: {self.sound}."
    
    def get_name(self):
        return f"Кличка: {self.name}."    

    def get_type(self):
        return f"Подвид : {self.pet_type}."    

    def __str__(self):
        return f"{self.get_name()} {self.get_type()} {self.get_sound()} Может {self.peculiarity}"

class Wheels(Car):

    sound = "лает"
    peculiarity = "сторожит"


class Engine(Car):

    sound = "мяукает"
    peculiarity = "ловит мышей"

class Doors(Car):

    sound = "мяукает"
    peculiarity = "ловит мышей"

if __name__ == "__main__":
    dog = Dog("Шарик", 3, "млекопитающие")
    cat = Cat("Мурка", 2, "млекопитающие")
    print(dog)
    print(cat)
    