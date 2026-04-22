# 9.14. Лотерея
import random

lottery_pool = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 'A', 'B', 'C', 'D', 'E']

winning_combination = random.sample(lottery_pool, 4)

# Выводим сообщение о выигрышной комбинации
print("=== ЛОТЕРЕЯ ===")
print(f"Выигрышная комбинация: {winning_combination}")
print("Любой билет, содержащий эту комбинацию из 4 элементов, является выигрышным!")