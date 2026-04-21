# 8.14. Автомобили

def make_car(manufacturer, model, **car_info):
    """Функция создает словарь с информацией об автомобиле"""

    car = {}
    car['manufacturer'] = manufacturer
    car['model'] = model
    for key, value in car_info.items():
        car[key] = value
    return car


car = make_car('subaru', 'outback', color='blue', tow_package=True)


print(car)


print(f"\nПроизводитель: {car['manufacturer']}")
print(f"Модель: {car['model']}")
print(f"Цвет: {car['color']}")
print(f"Пакет буксировки: {car['tow_package']}")