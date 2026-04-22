# 9.5. Попытки входа.

class User:
    """Класс пользователь"""
    def __init__(self, first_name, last_name, age=None, email=None):
        """Конструктор класса"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.email = email
        self.login_attempts = 0

    def describe_user(self):
        """Выводит сводку о пользователе"""
        print("========Сводка========")
        print(f"Имя: {self.first_name}")
        print(f"Фамилия: {self.last_name}")
        print(f"Возраст: {self.age}")
        print(f"Почта: {self.email}")

    def greet_user(self):
        """Метод приветствия пользователя"""
        print(f"Привет, {self.first_name}!")

    def increment_login_attempts(self):
        """Метод увеличивает значения login_attempts на 1"""
        self.login_attempts += 1

    def reset_login_attempts(self):
        """Метод обнуляет login_attempts"""
        self.login_attempts = 0


user3 = User('Анонимус','Анонимов')
print(user3.login_attempts)
user3.increment_login_attempts()
user3.increment_login_attempts()
user3.increment_login_attempts()
print(user3.login_attempts)
user3.reset_login_attempts()
print(user3.login_attempts)