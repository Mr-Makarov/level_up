from user import User
from pre import Privileges
class Admin(User):
    """Класс Админ"""
    def __init__(self, first_name, last_name, age=None, email=None):
        self.privileges = Privileges()