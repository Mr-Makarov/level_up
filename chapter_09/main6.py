# 9.6. Киоск с мороженым

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


class IceCreamStand(Restaurant):
    """"Класс киоск мороженного"""

    def __init__(self, restaurant_name, cuisine_type):
        self.flavors = ['Пломбир','Эскимо','Крем-брюле','Фруктовый лед','Ёжик']


    def show_flavors(self):
        """Метод выводит меню мороженного"""
        print("Мороженное в ассортименте:")
        print(*self.flavors, sep="\n")

restoran_ice = IceCreamStand("Русский мороз", "Киоск мороженного")
restoran_ice.show_flavors()
