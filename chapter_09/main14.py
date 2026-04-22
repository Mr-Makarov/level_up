# 9.13. Игра в кости.

from random import choice

class Die:
    """Класс кубик"""
    def __init__(self, sides=6):
        self.sides = sides

    def roll_die(self):
        return choice([i for i in range(1, self.sides + 1)])

k = Die()
print(k.roll_die())
print(k.roll_die())
print(k.roll_die())

print('\nk2')
k2 = Die(33)
print(k2.roll_die())
print(k2.roll_die())
print(k2.roll_die())
