# 8.7. Альбом.

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

albom1 = make_album(name='Ария', label='Герой асфальта')
albom2 = make_album(name='Ария', label='Крещение огнем',trek_list=10)
albom3 = make_album(name='Pantera', label='Cowboys from hell', trek_list=10)

print(albom1)
print(albom2)
print(albom3)