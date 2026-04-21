# 8.10. Отправка сообщений.

def send_messages(messages: list):
    """Функция получает на вход список сообщение перемешает их в другой список и возврашает оба списка """
    show_list = messages
    send_list = []

    while show_list:
        mes = show_list.pop(0)
        send_list.append(mes)
        print(mes)

    return show_list, send_list

list_messages = ['Первое сообщение ','Второе сообщение','Третье сообщение','Четвертое сообщение','Пятое сообщение']

show, send =  send_messages(list_messages)

print(show)
print(send)