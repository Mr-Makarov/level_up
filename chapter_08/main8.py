# 8.8. Альбом.

def make_album(name, label, trek_list=None):
    """Функция создания альбомов"""
    if trek_list:
        return {
            "name": f"{name}",
            "label": f"{label}",
            "trek_list": f"{trek_list}"
        }
    else:
        return {
            "name": f"{name}",
            "label": f"{label}"
        }

s = ''

while s != 'q':
    s = input("Добро пожаловать в конвеер альбомов(для запуска нажмите y для выхода q): ")
    if s == 'y':
        name = input("Укажите исполнителя: ")
        label = input("Укажите название альбома: ")
        trek_list = input("Укажите количество треков(опционально!): ")
        print(make_album(name, label, trek_list))
    else:
        s = 'q'
