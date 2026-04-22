# Создает для файла для задачи # 10.8. Кошки и собаки.
with open('cats.txt', 'w', encoding='utf-8') as f:
    f.write("Мурка\nБарсик\nСнежинка")

with open('dogs.txt', 'w', encoding='utf-8') as f:
    f.write("Шарик\nРекс\nДжек")