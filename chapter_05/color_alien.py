# Упр.5.3. Цвета пришельцев 1
lien_color = ['green', 'yellow', 'red']
if 'green' in lien_color:
    print("Вы получили 5 очков")

if 'green' not in lien_color:
    print("Вы получили 5 очков")

# Упр.5.4. Цвета пришельцев 2
if 'green' in lien_color:
    print("Вы получили 5 очков")
else:
    print("Вы получили 10 очков")

if 'green' not in lien_color:
    print("Вы получили 5 очков")
else:
    print("Вы получили 10 очков")

# Упр.5.5. Цвета пришельцев 3
print("1 версия")
if 'green' in lien_color:
    print("Вы получили 5 очков")
elif 'yellow' in lien_color:
    print("Вы получили 10 очков")
elif 'red' in lien_color:
    print("Вы получили 15 очков")

print("2 версия")
if 'green' not in lien_color:
    print("Вы получили 5 очков")
elif 'yellow' in lien_color:
    print("Вы получили 10 очков")
elif 'red' in lien_color:
    print("Вы получили 15 очков")

print("3 версия")
if 'green' not in lien_color:
    print("Вы получили 5 очков")
elif 'yellow' not in lien_color:
    print("Вы получили 10 очков")
elif 'red' in lien_color:
    print("Вы получили 15 очков")

