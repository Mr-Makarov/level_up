# 9.10. Импортирование класса

class Restaurant:
    """Класс ресторан"""
    def __init__(self, restaurant_name, cuisine_type):
        """Конструктор класса"""
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        """Выводит атрибуты класса"""
        print(self.restaurant_name, self.cuisine_type)


    def open_restaurant(self):
        """Метод выводит, что ресторан открыт"""
        print("Ресторан открыт!")