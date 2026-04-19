# 6.5. Реки.
rivers = {
    'Нил':'Египет',
    'Волга':'Россия',
    'Амазонка':'Бразилия',
    'Тенза':'Франция',
    'Янцзы':'Китай'
}

for river, contry in rivers.items():
    print(f"{river} протикает через {contry}.")

# 6.6. Опрос.
print('\n# 6.6. Опрос.')
favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'rust',
    'phil': 'python',
    }
users = ['jen', 'sarah',  'edward', 'phil', 'jon', 'max']

for user in users:
    if user in favorite_languages.keys():
        print(f'{user.title()} спасибо за участие!')
    else:
        print(f'{user.title()} пройдите наш опрос!')