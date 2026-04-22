#  9.1. Ресторан.

class Restaurant:
    """Класс ресторан"""
    def __init__(self):
        """Конструктор класса"""
        self.restaurant_name = "Елки палки"
        self.cuisine_type = 'Русская кухня'

    def describe_restaurant(self):
        """Выводит атрибуты класса"""
        print(self.restaurant_name, self.cuisine_type)


    def open_restaurant(self):
        """Метод выводит, что ресторан открыт"""
        print("Ресторан открыт!")

restaurant = Restaurant()

print(restaurant.restaurant_name)
print(restaurant.cuisine_type)
restaurant.describe_restaurant()
restaurant.open_restaurant()

