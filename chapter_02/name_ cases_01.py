# Упр  2.3 Личное сообщение
name = "Эрик"
mes = f"Здравствуйте, {name}, не хотите ли вы изучить Python сегодня?"

print(mes)

# Упр  2.4 Регистр символов в именах
name = "эрик"
print(name.lower())
print(name.upper())
print(name.title())

# Упр  2.5 Знаменитая цитата
mes = 'Альберт Эйнштейн однажды сказал: «Тот, кто никогда не совершал ошибок, ни \
когда не пробовал ничего нового».'
print(mes)

# Упр  2.6 Знаменитая цитата 2
famous_person = "Сократ"
message = f'{famous_person}: "Для мужчины стыдно состариться, так и не пожав сотку!"'
print(message)

# Упр  2.7 Удаление пробельных символов
name = "\tАнтон! \n"
print(name.lstrip())
print(name.rstrip())
print(name.strip())

# Упр 2.8. Расширения файлов
filename = 'python_notes.txt'
print(filename.removesuffix('.txt'))