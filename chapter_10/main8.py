# 10.9. Ошибки без уведомления.
def read_pets_silent(filename):
    """Читает файл с кличками, ошибки игнорирует"""
    try:
        with open(filename, 'r', encoding='utf-8') as f:
            contents = f.read()
            print(f"\nСодержимое файла {filename}:")
            print(contents)
    except FileNotFoundError:
        pass

# Читаем файлы (если файла нет - просто пропускаем)
read_pets_silent('cats.txt')
read_pets_silent('dogs.txt')
read_pets_silent('birds.txt')