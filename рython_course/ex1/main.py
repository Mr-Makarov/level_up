freinds = ['Иван', "Антон","Володя","Евгений","Михаил","Алексей"]

user_input = input("Введите имя: ")

if user_input.lower() in [i.lower() for i in freinds]:
    print("Вы угадали!")
else:
    print("Вы не угадали!")