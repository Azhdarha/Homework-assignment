"""Создайте класс Ship, который содержит информацию о корабле. С помощью механизма 
наследования, реализуйте класс Frigate (содержит информацию о фрегате), класс Destroyer 
(содержит информацию об эсминце), класс Cruiser (содержит информацию о крейсере). 
Каждый из классов должен содержать необходимые для работы методы."""

class Ship:
    name = "фрегате"
class Frigate(Ship):
    people = 300
ship = Frigate()
print(ship.name + " люди" + str(ship.people))


class Ship:
    name = "эсминце"
class Destroyer(Ship):
    people = 196
ship = Destroyer()
print(ship.name + " люди" + str(ship.people))

class Ship:
    name = "крейсере"
class Cruiser(Ship):
    people = 18
ship = Cruiser()
print(ship.name + " люди" + str(ship.people))