# 9.2. Три ресторана

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

restoran1 = Restaurant("Тануки", "Японская кухня")
restoran2 = Restaurant("Брынза", "Чебуречная")
restoran3 = Restaurant("Между булок", "Фаст фуд")

print("Ресторан 1")
print(restoran1.restaurant_name)
print(restoran1.cuisine_type)
restoran1.describe_restaurant()
restoran1.open_restaurant()

print("\nРесторан 2")
print(restoran2.restaurant_name)
print(restoran2.cuisine_type)
restoran2.describe_restaurant()
restoran2.open_restaurant()

print("\nРесторан 3")
print(restoran3.restaurant_name)
print(restoran3.cuisine_type)
restoran3.describe_restaurant()
restoran3.open_restaurant()