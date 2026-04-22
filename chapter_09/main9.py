# 9.9. Обновление аккумулятора

class Car:
    """Простая модель автомобиля"""

    def __init__(self, make, model, year):
        """Инициализация атрибутов автомобиля"""
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def get_descriptive_name(self):
        """Возвращает аккуратно отформатированное описание"""
        long_name = f"{self.year} {self.make} {self.model}"
        return long_name.title()

    def read_odometer(self):
        """Выводит пробег машины в милях"""
        print(f"This car has {self.odometer_reading} miles on it.")

    def update_odometer(self, mileage):
        """Устанавливает заданный пробег"""
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You can't roll back an odometer!")

    def increment_odometer(self, miles):
        """Увеличивает пробег на заданное значение"""
        self.odometer_reading += miles


class Battery:
    """Простая модель аккумулятора электромобиля"""

    def __init__(self, battery_size=40):
        """Инициализация атрибутов аккумулятора"""
        self.battery_size = battery_size

    def describe_battery(self):
        """Выводит информацию о мощности аккумулятора"""
        print(f"This car has a {self.battery_size}-kWh battery.")

    def get_range(self):
        """Выводит запас хода для аккумулятора"""
        if self.battery_size == 40:
            range = 150
        elif self.battery_size == 65:
            range = 225
        else:
            range = 0
            print("Unknown battery size!")

        print(f"This car can go about {range} miles on a full charge.")

    def upgrade_battery(self):
        """Обновляет аккумулятор до мощности 65, если она не равна 65"""
        if self.battery_size != 65:
            self.battery_size = 65
            print("Battery has been upgraded to 65 kWh!")
        else:
            print("Battery is already at maximum capacity (65 kWh).")


class ElectricCar(Car):
    """Представляет аспекты автомобиля, специфические для электромобилей"""

    def __init__(self, make, model, year):
        """Инициализация атрибутов класса-родителя"""
        super().__init__(make, model, year)
        self.battery = Battery()

    def describe_battery(self):
        """Выводит информацию о мощности аккумулятора"""
        self.battery.describe_battery()

    def get_range(self):
        """Выводит запас хода для аккумулятора"""
        self.battery.get_range()

my_tesla = ElectricCar('tesla', 'model s', 2022)
my_tesla.get_range()
my_tesla.battery.upgrade_battery()
my_tesla.get_range()