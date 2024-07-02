"""Создайте класс Device, который содержит информацию об устройстве. С помощью 
механизма наследования, реализуйте класс CoffeeMachine (содержит информацию о 
кофемашине), класс Blender (содержит информацию о блендере), класс MeatGrinder 
(содержит информацию о мясорубке). Каждый из классов должен содержать необходимые 
для работы методы."""

class Device:
    def __init__(self, device, brand, volume, consumption):
        self.Device = Device
        self.brand = brand
        self.volume = volume
        self.consumption
        
    def get_sound(self):
        return f"{self.__class__.__Device__}: {self.action}."

    def get_name(self):
        return f"Устройство: {self.device}."

    def get_type(self):
        return f"Марка: {self.brand}."

    def __str__(self):
        return f"{self.get_device()} {self.get_brand()} {self.get_volume()} {self.get_consumption} Может {self.peculiarity}"

class CoffeeMachine(Device):
    peculiarity = "варет кофе"


class Blender(Device):
    peculiarity = "делает напитки"

class MeatGrinder(Device):
     peculiarity = "мясорубка"

if __name__ == "__main__":
    coffeemachine = CoffeeMachine("Кофемашина")
    blender = Blender("Блендер")
    meatgrinder = MeatGrinder("Блендер")
    print(coffeemachine)
    print(blender)
    print(meatgrinder)