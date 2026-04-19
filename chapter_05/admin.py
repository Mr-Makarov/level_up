# Упр 5.8. Здравствуйте, админ!
print('# Упр 5.8. Здравствуйте, админ!')
user_list = ['admin','admin_web','Иванов','admin_mail','Петров']

for user in user_list:
    if 'admin' in user:
        print(f"Здравствуйте, {user}, хотите просмотреть отчет о состоянии дел?")
    else:
        print(f"Привет, {user}, спасибо, что авторизовался в системе")

# Упр 5.9. Нет пользователей.
user_list_clean = []

if not user_list_clean:
    print("Нам нужно добавить несколько пользователей!")


# Упр 5.10. Проверка имен пользователей.
print('\n# Упр 5.10. Проверка имен пользователей.')
current_users = ['uSer_1','USER_2','user_3','UseR_4','user_5']
new_users = ['user_22','USER_2','user_33','USER_4','user_5']

for user in new_users:
    if user.lower() in [i.lower() for i in current_users]:
        print(f"Имя {user} уже используется в системе! Выберете другое.")
    else:
        print(f"Имя {user} свободно!")

# Упр 5.11. Порядковые числительные.
print('\n# Упр 5.11. Порядковые числительные.')
digits = [i for i in range(1, 10)]
for i in digits:
    if i == 1:
        print(f'{i}st')
    elif i == 2:
        print(f'{i}nd')
    elif i == 2:
        print(f'{i}rd')
    else:
        print(f'{i}th')
