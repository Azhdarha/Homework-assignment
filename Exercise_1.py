class Car():
    """Описание автомобиля"""
    def __init__(self, model, years, brand, engine, colour,price):
        """Инициализирует атрибуты"""
        self.model = model
        self.years = years
        self.brand = brand
        self.engine = engine
        self.colour = colour
        self.price = price
        self.mileage = 0

    def get_full_name(self):
        """Автомобиль"""
        name = f"Автомобиль {self.model} {self.years} {self.brand} {self.engine} {self.colour} {self.price}"
        return name.title()

    def read_mileage(self):
        """Пробег автомобиля"""
        print(f"Пробег автомобиля {self.mileage} км.")