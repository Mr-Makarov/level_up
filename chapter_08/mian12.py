# 8.10. Отправка сообщений.

def send_messages(messages: list):
    """Функция получает на вход список сообщение и делает его копию."""
    show_list = messages
    backup_list = []

    for i in  show_list:
        backup_list.append(i)

    return show_list, backup_list

list_messages = ['Первое сообщение ','Второе сообщение','Третье сообщение','Четвертое сообщение','Пятое сообщение']

show, backup =  send_messages(list_messages)

print(show)
print(backup)