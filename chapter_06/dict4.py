cities = {
    'токио': {
        'country': 'япония',
        'population': 13960000,
        'area_km2': 2194,
        'fact': 'В Токио находится самый загруженный пешеходный переход в мире - Сибуя.',
        'landmarks': ['императорский дворец', 'башня токио', 'храм сэнсо-дзи'],
        'famous_food': ['суши', 'рамен', 'тян', 'такояки'],
    },
    'париж': {
        'country': 'франция',
        'population': 2160000,
        'area_km2': 105,
        'fact': 'Эйфелева башня перекрашивается каждые 7 лет для защиты от ржавчины.',
        'landmarks': ['эйфелева башня', 'лувр', 'нотр-дам', 'монмартр'],
        'famous_food': ['круассан', 'багет', 'утиное конфи', 'макаронс'],
    },
    'рио-де-жанейро': {
        'country': 'бразилия',
        'population': 6780000,
        'area_km2': 1221,
        'fact': 'Статуя Христа-Искупителя является одним из новых семи чудес света.',
        'landmarks': ['статуя христа-искупителя', 'пляж копакабана', 'гора сахарная голова'],
        'famous_food': ['фейжоада', 'кайпиринья', 'пао-де-кейжу'],
    },
}

for city, info in cities.items():
    print("\n" + "=" * 50)
    print(f"Город: {city.title()}")
    print("=" * 50)

    print(f"Страна: {info['country'].title()}")
    print(f"Население: {info['population']:,} человек")
    print(f"Площадь: {info['area_km2']} км²")

    # Плотность населения
    density = info['population'] / info['area_km2']
    print(f"Плотность населения: {density:.0f} чел/км²")

    print(f"Интересный факт: {info['fact']}")

    # Достопримечательности
    if len(info['landmarks']) == 1:
        print(f"Достопримечательности: {info['landmarks'][0].title()}")
    elif len(info['landmarks']) == 2:
        print(f"Достопримечательности: {info['landmarks'][0].title()} и {info['landmarks'][1].title()}")
    else:
        print(
            f"Достопримечательности: {info['landmarks'][0].title()}, {info['landmarks'][1].title()} и {info['landmarks'][2].title()}")

    # Известная еда
    if len(info['famous_food']) == 1:
        print(f"Известная еда: {info['famous_food'][0].title()}")
    elif len(info['famous_food']) == 2:
        print(f"Известная еда: {info['famous_food'][0].title()} и {info['famous_food'][1].title()}")
    else:
        print(
            f"Известная еда: {info['famous_food'][0].title()}, {info['famous_food'][1].title()} и {info['famous_food'][2].title()}")

print("\n" + "=" * 50)
print("Программа завершена")
print("=" * 50)