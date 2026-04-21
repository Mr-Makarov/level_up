# 8.12. Бутерброды

def make_sandwich(*ingredients):
    """Функция для описания заказанного бутерброда"""
    print("\nПриготовлен бутерброд со следующими компонентами:")
    for ingredient in ingredients:
        print(f"- {ingredient}")


make_sandwich('ветчина', 'сыр', 'салат')
make_sandwich('курица', 'помидор', 'огурец', 'майонез')
make_sandwich('масло', 'икра')