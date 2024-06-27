class Book():
    """Описание книги"""
    def __init__(self, brand, model, years):
        """атрибуты книги"""
        self. title =  title
        self.years = years
        self.publisher = publisher
        self.genre = genre
        self.author = author
        self.price = price


    def get_full_name(self):
        """книга"""
        name = f"книга {self.title} {self.years} {self.publisher} {self.genre} {self.author} {self.price}"
        return name.title()