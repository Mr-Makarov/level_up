# 10.1 Изучение Python
from pathlib import Path

path = Path("learning_python.txt")
content = path.read_text(encoding='utf-8').splitlines()
new_list = []

for i in content:
    print(i)
    new_list.append(i)

print()
print(new_list)

