def main():
    to_do = []
    while True:
        command = input("1 - Добавить\n2 - Удалить\n3 - Просмотр\n4 - Изменить\nВведите команду: ")
        if command == "1":
            name = input("Введите задачу: ")
            to_do.append(name)
        elif command == '2':
            number = input("Введите номер задачи: ")
            task = to_do.pop(number)
            print(f"Задача '{task}' удалена!")
        elif command == '3':
            print("Мой список дел!")
            for i, task in enumerate(to_do):
                print(f"{i} - {task}")
            print("="*15)
        elif command == '4':
            number = int(input("Введите номер задачи: "))
            task = input("Введите задачу: ")
            to_do[number] = task

main()