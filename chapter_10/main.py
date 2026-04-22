# 10.5. Гостевая книга
from pathlib import Path

path = Path("guest_book.txt")

s = ''

while s != 'q':

    name = input("Введите ваше имя: ")
    print(f"Добро пожаловать, {name.title()}!")

    with open(path, 'a', encoding="utf-8") as file:
        file.write(f"{name} посетил(а) гостевую книгу.\n")

    s = input("Для выхода введите 'q' (Enther для продолжения): ")

