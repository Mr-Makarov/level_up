# 9.11. Импортирование класса

from user import User, Privileges, Admin


admin = Admin('Admin','Local','','admin@admin.ru')
admin.privileges.show_privileges()

print()
user3 = User('Анонимус','Анонимов')
user3.describe_user()