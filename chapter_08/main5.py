# 8.5. Города.

def describe_city(city_name, country='неизвестной стране'):
    """Выводит информацию о местонахождении города."""
    print(f"{city_name} находится в {country}")

# Вызовы функции
describe_city('Рейкьявик', 'Исландии')
describe_city('Москва', 'России')
describe_city('Лиссабон')