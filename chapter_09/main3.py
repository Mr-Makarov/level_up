# 9.3. Пользователи

class User:
    """Класс пользователь"""
    def __init__(self, first_name, last_name, age=None, email=None):
        """Конструктор класса"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.email = email

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

print('user1')
user1 = User('Антон','Иванов','32','ianton@domen.ru')
user1.greet_user()
user1.describe_user()

print('\nuser2')
user2 = User('Иван','Антонов','23','ivan@domen.ru')
user2.greet_user()
user2.describe_user()

print('\nuser3')
user3 = User('Ананимус','Ананимов')
user3.greet_user()
user3.describe_user()


