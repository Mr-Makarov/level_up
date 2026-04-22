# 10.12. Сохраненное любимое число
import json

def load_favorite_number():
    """Загружает число из файла"""
    try:
        with open('favorite_number.json', 'r') as f:
            return json.load(f)
    except FileNotFoundError:
        return None


number = load_favorite_number()

if number:
    print(f"Я знаю ваше любимое число! Это {number}.")
else:
    number = input("Какое ваше любимое число? ")
    with open('favorite_number.json', 'w') as f:
        json.dump(number, f)

    print(f"Число {number} сохранено!")
