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
