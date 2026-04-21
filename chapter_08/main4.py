# 8.4. Большие футболки.

def make_shirt(t='Я люблю Python', s='L'):
    """Функция с параметрами по умолчанию"""
    print(f'Текст футболки: {t}')
    print(f'Размер: {s}')

make_shirt()

make_shirt(t='Я люблю Linux', s='XL')