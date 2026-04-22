# 10.11. Любимое число.

import json

number = input("Какое ваше любимое число? ")

with open('favorite_number.json', 'w') as f:
    json.dump(number, f)

print(f"Число {number} сохранено!")