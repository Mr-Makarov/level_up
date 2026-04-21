# 8.13. Профиль

def build_profile(first, last, **user_info):
    """Функция строит словарь с информацией о пользователе"""

    profile = {}
    profile['first_name'] = first
    profile['last_name'] = last
    for key, value in user_info.items():
        profile[key] = value
    return profile

my_profile = build_profile(
    'Иван',
    'Петров',
    age=30,
    city='Москва',
    profession='программист'
)

print(my_profile)