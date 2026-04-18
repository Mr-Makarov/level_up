# Упр 4.1. Пицца
print("# Упр 4.1. Пицца")
pizza = ['моцарелла','пеперони','гавайская']

for i in pizza:
    print(f"Я люблю пиццу {i}!")
print("Я очень люблю пиццу!»")

# Упр 4.2. Животные
print("# Упр 4.2. Животные")
animals = ['Кот','Собака','Конь']
for k in animals:
    print(f"{k} — отличное домашнее животное")
print("Любое из этих животных — отличное домашнее животное!")

# Упр 4.3.  Считаем до 20.
print("# Упр 4.3.  Считаем до 20.")
for r in range(1, 21):
    print(r)

# Упр 4.4. Миллион
print("# Упр 4.4. Миллион")
one_million = [i for i in range(1, 1000001)]
for d in one_million[:10]:
    print(d)

# Упр 4.5. Суммирование миллиона чисел.
print("# Упр 4.5. Суммирование миллиона чисел.")
one_million = [i for i in range(1, 1000001)]
print("Самое маленькое число списка:",min(one_million))
print("Самое большое число:", max(one_million))
print("Сумма миллиона чисел:", sum(one_million))

# Упр 4.6. Нечетные числа.
print("# Упр 4.6. Нечетные числа.")
list_2= [i for i in range(1, 21, 2)]
for l in list_2:
    print(l)

# Упр 4.7. Тройки.
print("# Упр 4.7. Тройки.")
list_3 = [i for i in range(3, 31, 3)]
for l in list_3:
    print(l)
# Упр 4.8. Кубы.
print('# Упр 4.8. Кубы.')
list_4 = [i ** 2 for i in range(1, 11)]
for y in list_4:
    print(y)

# Упр 4.10. Срезы.
print('# Упр 4.10. Срезы.')
print(f"Привет первые три элемента списка это: {one_million[:3]}")
print(f"Привет три средних элемента списка это: {one_million[int(len(one_million) / 2):int(len(one_million) / 2 + 3)]}")
print(f"Привет три последних элемента списка это:{sorted(one_million, reverse=True)[:3]}")

# Упр 4.11. Моя пицца, твоя пицца
print("# Упр 4.11. Моя пицца, твоя пицца")

pizza = ['моцарелла','пеперони','гавайская']
friend_pizzas = pizza[:]

pizza.append("Мясная")
friend_pizzas.append("Неополитанская")

print("Моя любимая пицца:")
for p in pizza:
    print(p.title(), end=' ')
print()

print("Любимая пицца друга:")
for f in friend_pizzas:
    print(f.title(), end=' ')

# 4.13. Шведский стол
print("# 4.13. Шведский стол")
my_tuple = ('яичница','оливье','овсянка','сырники','мороженное')
for i in my_tuple:
    print(i)

#my_tuple[0] = "Борщ"
new_tuple = ('яичница','гречка','овсянка','сырники','яблоко')
for i in new_tuple:
    print(i)

# Упр 4.7. Тройки.
# Упр 4.7. Тройки.
# Упр 4.7. Тройки.
# Упр 4.7. Тройки.
# Упр 4.7. Тройки.
# Упр 4.7. Тройки.
# Упр 4.7. Тройки.