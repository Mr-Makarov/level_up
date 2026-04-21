# 8.9. Сообщения

def show_messages(messages: list):
    """Функция получает на вход список сообщение и выводит их по одному"""

    for mes in messages:
        print(mes)

list_messages = ['Первое сообщение ','Второе сообщение','Третье сообщение','Четвертое сообщение','Пятое сообщение']

show_messages(list_messages)