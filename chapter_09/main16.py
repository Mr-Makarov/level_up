# 9.15. Анализ лотереи

import random

lottery_pool = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 'A', 'B', 'C', 'D', 'E']

winning_combination = random.sample(lottery_pool, 4)

print("=== АНАЛИЗ ЛОТЕРЕИ ===")
print(f"Выигрышная комбинация: {winning_combination}")
print("\nНачинаем поиск выигрышного билета...")

my_ticket = [3, 7, 'B', 'E']

print(f"Мой билет: {my_ticket}\n")

attempts = 0
won = False

while not won:
    random_combination = random.sample(lottery_pool, 4)
    attempts += 1

    if sorted([str(i) for i in random_combination]) == sorted([str(i) for i in winning_combination]):
        won = True
        print(f"ВЫИГРЫШ! Найдена выигрышная комбинация!")
        print(f"Выигрышная комбинация: {random_combination}")
        print(f"Количество попыток: {attempts}")
        break

print(f"\nСтатистика:")
print(f"Всего потребовалось {attempts} попыток, чтобы выиграть в лотерею.")