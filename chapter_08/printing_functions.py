# 8.15. Печать моделей.

def print_models(unprinted_designs, completed_models):
    """
    Имитирует печать моделей, пока список не станет пустым.
    Каждая модель после печати перемещается в completed_models.
    """
    while unprinted_designs:
        current_design = unprinted_designs.pop()
        print(f"Печать модели: {current_design}")
        completed_models.append(current_design)

def show_completed_models(completed_models):
    """Выводит информацию о напечатанных моделях."""
    print("\nСледующие модели были напечатаны:")
    for model in completed_models:
        print(model)