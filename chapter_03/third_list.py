# Упр 3.8. Повидать мир.
countries = ['КНР','Бразилия','Куба','Мексика','Грузия']
print(countries)
print(sorted(countries))
print(countries)
print(sorted(countries, reverse=True))
print(countries)
countries.sort()
print(countries)
countries.sort(reverse=True)
print(countries)

# Упр 3.9. Количество гостей.
print(f"Количество стран: {len(countries)}")



# 3.10. Все функции
# Создание списка языков программирования
languages = ["Python", "Java", "C++", "JavaScript", "Go", "Rust"]

print("Исходный список языков:")
print(languages)
print()

# 1. len() - длина списка
print(f"1. Количество языков в списке: {len(languages)}")

# 2. append() - добавление элемента в конец
languages.append("Swift")
print(f"2. После append('Swift'): {languages}")

# 3. insert() - вставка элемента по индексу
languages.insert(2, "Kotlin")
print(f"3. После insert(2, 'Kotlin'): {languages}")

# 4. remove() - удаление элемента по значению
languages.remove("Java")
print(f"4. После remove('Java'): {languages}")

# 5. pop() - удаление и возврат элемента по индексу
removed = languages.pop(3)
print(f"5. После pop(3) удален '{removed}': {languages}")

# 6. sort() - сортировка списка
languages.sort()
print(f"6. После sort() (по алфавиту): {languages}")

# 7. reverse() - обратный порядок
languages.reverse()
print(f"7. После reverse(): {languages}")

# 8. sorted() - временная сортировка
temp_sorted = sorted(languages)
print(f"8. Временная сортировка (sorted): {temp_sorted}")
print(f"    Оригинал не изменился: {languages}")

# 9. del - удаление элемента или среза
del languages[0]
print(f"9. После del languages[0]: {languages}")

print("\nФинальный список языков:")
print(languages)