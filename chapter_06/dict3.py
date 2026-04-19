# 6.7. Люди
print("6.7. Люди")
person1 = {
    'first_name': "Максим",
    "last_name":"Макаров",
    "age":"38",
    "city":"Москва"
}

person2= {
    'first_name': "Иван",
    "last_name":"Ивано",
    "age":"32",
    "city":"Казань"
}

person3 = {
    'first_name': "Антон",
    "last_name":"Большой",
    "age":"48",
    "city":"Тула"
}

people = [person1, person2, person3]

for person in people:
    for l, k in person.items():
        print(l, k)
    print()

# 6.9. Любимые места
print("6.9. Любимые места")
favorite_places = {
    'алексей': ['горы', 'озеро байкал', 'парк'],
    'мария': ['море', 'пляж'],
    'иван': ['лес', 'река', 'дача'],
}
for name, places in favorite_places.items():
    if len(places) == 1:
        print(f"{name.title()} любит место: {places[0].title()}")
    else:
        places_str = ', '.join([place.title() for place in places])
        print(f"{name.title()} любит места: {places_str}")

# 6.10. Любимые числа
print("\n6.10. Любимые числа")
favorite_numbers = {
    'алексей': [7, 42, 13],
    'мария': [3, 8],
    'иван': [21],
    'елена': [5, 12, 99, 1],
    'дмитрий': [777, 13],
}
for name, numbers in favorite_numbers.items():
    if len(numbers) == 1:
        print(f"{name.title()}, любимое число: {numbers[0]}")
    else:
        numbers_str = ', '.join(str(num) for num in numbers)
        print(f"{name.title()}, любимые числа: {numbers_str}")

# 6.11. Города.
print("\n6.11. Города.")

cities = {
    'токио': {
        'country': 'япония',
        'population': '13.96 млн',
        'fact': 'В Токио находится самый загруженный пешеходный переход в мире - Сибуя.',
    },
    'париж': {
        'country': 'франция',
        'population': '2.16 млн',
        'fact': 'Эйфелева башня перекрашивается каждые 7 лет для защиты от ржавчины.',
    },
    'рио-де-жанейро': {
        'country': 'бразилия',
        'population': '6.78 млн',
        'fact': 'Статуя Христа-Искупителя является одним из новых семи чудес света.',
    },
}

for city, info in cities.items():
    print(f"\nГород: {city.title()}")
    print(f"  Страна: {info['country'].title()}")
    print(f"  Население: {info['population']} человек")
    print(f"  Интересный факт: {info['fact']}")

