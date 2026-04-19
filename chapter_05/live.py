# Упр.5.6. Периоды жизни
age = 45

if age < 2:
    print("Младенец")
elif 2 <= age < 4:
    print("Младенец")
elif 4 <= age < 13:
    print("Ребенок")
elif 13 <= age < 20:
    print("Подросток")
elif 20 <= age < 65:
    print("Взрослый")
else:
    print("Пожилой человек")

# Упр.5.7. Любимый фрукт.
fruits = ['яблоко','банан','виноград']

for fruit in fruits:
    if fruit == 'яблоко' or fruit == 'банан':
        print(f"Я очень люблю {fruit}", )