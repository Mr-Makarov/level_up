# 9.4. Посетители

class Restaurant:
    """Класс ресторан"""
    def __init__(self, restaurant_name, cuisine_type):
        """Конструктор класса"""
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0

    def describe_restaurant(self):
        """Выводит атрибуты класса"""
        print(self.restaurant_name, self.cuisine_type)


    def open_restaurant(self):
        """Метод выводит, что ресторан открыт"""
        print("Ресторан открыт!")

    def set_number_served(self, atr):
        """Метод изменения number_served"""
        self.number_served = atr

    def increment_number_served(self, atr):
        """Метод увеличивает number_served"""
        self.number_served += atr

restaurant = Restaurant("Брынза", "Чебуречная")

print(restaurant.number_served)
restaurant.number_served = 5
print(restaurant.number_served)
restaurant.set_number_served(12)
print(restaurant.number_served)
restaurant.increment_number_served(100)
print(restaurant.number_served)