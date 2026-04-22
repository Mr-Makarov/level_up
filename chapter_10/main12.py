# 10.13. Словарь пользователя.

import json


def get_user_info():
    """Запрашивает информацию о пользователе"""
    print("Пожалуйста, введите информацию о себе:")
    name = input("Ваше имя: ")
    age = input("Ваш возраст: ")
    city = input("Ваш город: ")

    user_dict = {
        'name': name,
        'age': age,
        'city': city
    }
    return user_dict


def save_user_info(user_dict):
    """Сохраняет словарь пользователя в файл"""
    with open('user_info.json', 'w', encoding='utf-8') as f:
        json.dump(user_dict, f, ensure_ascii=False, indent=4)


def load_user_info():
    """Загружает словарь пользователя из файла"""
    try:
        with open('user_info.json', 'r', encoding='utf-8') as f:
            return json.load(f)
    except FileNotFoundError:
        return None


def show_user_info():
    """Основная логика программы"""
    user_info = load_user_info()

    if user_info:
        print("\n--- Данные о пользователе ---")
        print(f"Имя: {user_info['name']}")
        print(f"Возраст: {user_info['age']}")
        print(f"Город: {user_info['city']}")
    else:
        user_info = get_user_info()
        save_user_info(user_info)
        print("\nДанные сохранены!")
        print(f"Сохранена следующая информация: {user_info}")


# Запуск программы
show_user_info()