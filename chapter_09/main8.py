# 9.8. Привилегии.


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


class Privileges:
    """Класс управления привилегиями"""
    def __init__(self):

        self.privileges = [
            "разрешено добавлять сообщения",
            "разрешено удалять пользователей",
            "разрешено блокировать пользователей"
        ]

    def show_privileges(self):
        """Метод вывода привилегий"""
        for i in self.privileges:
            print(i)



class Admin(User):
    """Класс Админ"""
    def __init__(self, first_name, last_name, age=None, email=None):
        self.privileges = Privileges()




admin = Admin('Admin','Local','','admin@admin.ru')
admin.privileges.show_privileges()
