# 9.12. Множественные модули.
from user import User
from admin import Admin



admin = Admin('Admin','Local','','admin@admin.ru')
admin.privileges.show_privileges()

print()
user3 = User('Анонимус','Анонимов')
user3.describe_user()