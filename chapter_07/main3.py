# 7.8. Бутерброды
sandwich_orders = ['тунец', 'курица', 'сырный', 'ветчина', 'овощной']
finished_sandwiches = []

while sandwich_orders:
    current_sandwich = sandwich_orders.pop()
    print(f"Я приготовил бутерброд с {current_sandwich}.")
    finished_sandwiches.append(current_sandwich)

print("\n--- Все приготовленные бутерброды ---")
for sandwich in finished_sandwiches:
    print(f"Бутерброд с {sandwich}")


# 7.9. Без пастромы
print("\n# 7.9. Без пастромы")
sandwich_orders = ['pastrami', 'тунец', 'pastrami', 'курица', 'pastrami', 'сырный', 'ветчина']
finished_sandwiches = []

print("Извините, пастрома закончилась!")

while 'pastrami' in sandwich_orders:
    sandwich_orders.remove('pastrami')

print("\n--- Готовим бутерброды ---")
while sandwich_orders:
    current_sandwich = sandwich_orders.pop()
    print(f"Я приготовил бутерброд с {current_sandwich}.")
    finished_sandwiches.append(current_sandwich)

print("\n--- Все приготовленные бутерброды ---")
for sandwich in finished_sandwiches:
    print(f"Бутерброд с {sandwich}")

if 'pastrami' not in finished_sandwiches:
    print("\nУспешно! Ни один бутерброд с пастромой не был приготовлен.")

# Словарь для хранения результатов опроса
responses = {}

# Флаг для продолжения опроса
polling_active = True

print("Опрос: Куда бы вы хотели поехать в отпуск?")
print("(Для выхода введите 'выход')\n")

while polling_active:
    # Запрашиваем имя пользователя
    name = input("Как вас зовут? ")

    if name.lower() == 'выход':
        polling_active = False
        break

    # Запрашиваем место, где хочет побывать пользователь
    place = input("Если бы вы могли посетить одно место в мире, то куда бы отправились? ")

    if place.lower() == 'выход':
        polling_active = False
        break

    # Сохраняем ответ
    responses[name] = place

    # Спрашиваем, хочет ли кто-то еще пройти опрос
    repeat = input("Хотите ли вы опросить еще кого-то? (да/нет): ")
    if repeat.lower() == 'нет':
        polling_active = False

# Выводим результаты опроса
print("\n" + "=" * 50)
print("РЕЗУЛЬТАТЫ ОПРОСА ОБ ОТПУСКЕ МЕЧТЫ")
print("=" * 50)

if responses:
    for name, place in responses.items():
        print(f"{name.title()} мечтает посетить {place.title()}!")

    # Дополнительная статистика
    print("\n--- Спасибо за участие! ---")
    print(f"Всего опрошено: {len(responses)} человек(а)")
else:
    print("Нет результатов опроса.")