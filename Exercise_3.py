class Stadium():
    """Стадион"""
    def __init__(self, model, years, brand, engine, colour,price):
        """атрибуты Стадиона"""
        self.title = title
        self.date = date
        self.country = country
        self.city = city
        self.capacity = 0

    def get_full_name(self):
        """Стадион"""
        name = f"Стадион {self.title} {self.date} {self.country} {self.city}"
        return name.title()

    def read_mileage(self):
        """вместимость стадиона"""
        print(f"вместимость стадиона {self.capacity}")