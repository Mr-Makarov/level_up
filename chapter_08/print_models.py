# 8.16. Импортирование

from printing_functions import print_models, show_completed_models

# Создание списков
unprinted_designs = ['phone case', 'robot pendant', 'dodecahedron']
completed_models = []

# Печать моделей
print_models(unprinted_designs, completed_models)
show_completed_models(completed_models)