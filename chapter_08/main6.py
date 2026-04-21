# 8.6. Названия городов

def city_country(city, country):
    """Функция получает на вход город и страну и
    возвращает их в формате  город, страну"""

    return f'{city}, {country}'


print(city_country('Москва', "Россия"))
print(city_country('Токио', "Япония"))
print(city_country('Минкс', "Беларусь"))