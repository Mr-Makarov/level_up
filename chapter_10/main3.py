# 10.4. Гость

from pathlib import Path

path = Path("guest.txt")

name = input("Введите ваше имя: ")

write_name = path.write_text(name, encoding="utf-8")