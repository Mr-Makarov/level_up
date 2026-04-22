# 10.7. Калькулятор.

while True:
    try:
        num1 = int(input("\nВведите первое число: "))
        num2 = int(input("Введите второе число: "))
        result = num1 + num2
        print(f"Результат: {num1} + {num2} = {result}")

        # Запрашиваем продолжение
        cont = input("Продолжить? (y/n): ").lower()
        if cont != 'y':
            break
    except ValueError:
        print("Ошибка! Введите корректные числа.")


print("Программа завершена.")