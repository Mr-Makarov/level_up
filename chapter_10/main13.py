# 10.14. Проверка пользователя

import json

def get_stored_username():
    """Получает сохранённое имя пользователя, если оно существует"""
    try:
        with open('username.json', 'r') as f:
            username = json.load(f)
    except FileNotFoundError:
        return None
    else:
        return username


def get_new_username():
    """Запрашивает новое имя пользователя"""
    username = input("Как вас зовут? ")
    with open('username.json', 'w') as f:
        json.dump(username, f)
    return username


def greet_user():
    """Приветствует пользователя с проверкой личности"""
    username = get_stored_username()

    if username:
        # Спрашиваем, правильно ли определено имя
        print(f"Это {username}?")
        answer = input("Вы тот самый пользователь? (да/нет): ").lower()

        if answer == 'да' or answer == 'yes' or answer == 'y':
            print(f"С возвращением, {username}!")
        else:
            # Если пользователь не тот, запрашиваем новое имя
            username = get_new_username()
            print(f"Мы запомним вас, {username}. Приятно познакомиться!")
    else:
        # Если файла нет, запрашиваем имя впервые
        username = get_new_username()
        print(f"Мы запомним вас, {username}. Приятно познакомиться!")


# Запуск программы
greet_user()