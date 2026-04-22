# 10.8. Кошки и собаки.
def read_pets(filename):
    """Читает файл с кличками и выводит содержимое"""
    try:
        with open(filename, 'r', encoding='utf-8') as f:
            contents = f.read()
            print(f"\nСодержимое файла {filename}:")
            print(contents)
    except FileNotFoundError:
        print(f"Ошибка: Файл '{filename}' не найден!")

# Читаем оба файла
read_pets('cats.txt')
read_pets('dogs.txt')