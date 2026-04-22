# 10.2 10.2. Изучение C
from pathlib import Path

path = Path("learning_python.txt")
content = path.read_text(encoding='utf-8').splitlines()
new_list = []

for i in content:
    print(i.replace("Python", "C"))



