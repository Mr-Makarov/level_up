def count_phrase_in_file(filename, phrase):
    """Подсчитывает количество вхождений фразы в файле"""
    try:
        with open(filename, 'r', encoding='utf-8') as f:
            contents = f.read().lower()
            return contents.count(phrase.lower())
    except FileNotFoundError:
        return -1 # Если файл не найден вернуть -1

filename = 'book.txt'
phrase = 'Ship'

count = count_phrase_in_file(filename, phrase)
if count >= 0:
    print(f"Фраза '{phrase}' встречается {count} раз в файле {filename}")
else:
    print(f"Файл {filename} не найден")