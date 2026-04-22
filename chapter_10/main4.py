# 10.6. Сложение.
try:
    num1 = int(input("Введите первое число: "))
    num2 = int(input("Введите второе число: "))
    result = num1 + num2
    print(f"Результат сложения: {num1} + {num2} = {result}")
except ValueError:
    print("Ошибка! Пожалуйста, вводите только числа.")