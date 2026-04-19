# 7.10. Отпуск мечты
responses = {}


polling_active = True

print("Опрос: Куда бы вы хотели поехать в отпуск?")
print("(Для выхода введите 'выход')\n")

while polling_active:
    name = input("Как вас зовут? ")

    if name.lower() == 'выход':
        polling_active = False
        break

    place = input("Если бы вы могли посетить одно место в мире, то куда бы отправились? ")

    if place.lower() == 'выход':
        polling_active = False
        break

    responses[name] = place

    repeat = input("Хотите ли вы опросить еще кого-то? (да/нет): ")
    if repeat.lower() == 'нет':
        polling_active = False

print("\n" + "=" * 50)
print("РЕЗУЛЬТАТЫ ОПРОСА ОБ ОТПУСКЕ МЕЧТЫ")
print("=" * 50)

if responses:
    for name, place in responses.items():
        print(f"{name.title()} мечтает посетить {place.title()}!")

    print("\n--- Спасибо за участие! ---")
    print(f"Всего опрошено: {len(responses)} человек(а)")
else:
    print("Нет результатов опроса.")