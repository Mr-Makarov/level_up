class CoffeeMachine:
    """Клас кофе машина"""
    def __init__(self):
        self.menu = {
            'эспрессо*2': {'price': 100, 'volume': 60, 'resources': 1000},
            'американо': {'price': 120, 'volume': 250, 'resources': 100},
            'капучино': {'price': 150, 'volume': 250, 'resources': 1000},
            'латте': {'price': 200, 'volume': 300, 'resources': 1000},
        }

        self.bank = {'100': 100, '500': 100, '50': 300, '1000': 10}
        # Общая сумма денег в кофе машине
        self.bank_sum = sum(int(nominal) * count for nominal, count in self.bank.items())
        # Атрибуты хранящие пользовательский заказ, по умолчанию пустые
        self._user_coffe = None
        self._user_coffee_volume = None
        self._user_debt = None


    def display_menu(self):
        """Метод выводи меню для покупателя"""
        number = 0
        print("=====Выберите напиток=====")
        for cof in self.menu:
            number += 1
            print(f"{number} - {cof} цена: {self.menu[cof]['price']}, объем: {self.menu[cof]['volume']}.")
        print("==========================")


    def request_order(self):
        """Запрашивает у клиента заказ, а затем выводит, название объем и стоимость."""
        order_menu = {
            1: 'эспрессо*2',
            2: 'американо',
            3: 'капучино',
            4: 'латте'
        }

        while True:
            request = int(input('Введите номер напитка: '))

            type_coffee = order_menu[request]
            volume_order = self.menu[type_coffee]["volume"]
            price = self.menu[type_coffee]["price"]

            # Проверяем остался ли кофе
            if volume_order <= self.menu[type_coffee]["resources"]:
                # Если да выводим заказ и стоимость
                print(f"Ваш заказ: {type_coffee} - {volume_order} мл.")
                print(f"К отплате: {price} рублей")
                break
            else:
                # Если нет, предлагаем другой напиток
                print(f"Извините {type_coffee} закончился")
                print("Хотите выбрать другой напиток?")
                new_order = input("да/нет: ")
                # Если пользователь не хочет другой, прощаемся
                if new_order == 'нет':
                    print("Всего хорошего!")
                    break

        # Записываем заказ клиента
        self._user_coffe = type_coffee
        self._user_coffee_volume = volume_order
        self._user_debt = price


    def calculate_change(self, change_amount):
        """Метод рассчитывает сдачу разным номиналом и обновляет их в банке"""

        # Сортируем номиналы от большего к меньшему
        sorted_nominal = sorted([int(n) for n in self.bank.keys()], reverse=True)

        # Словарь для хранения купюр на выдачу
        change_nodes = {}
        remaining_change = change_amount

        # Создаем временный банк для временного использования
        temp_bank = {int(nominal): count for nominal, count in self.bank.items()}

        # Рассчитываем сдачу
        for nominal in sorted_nominal:
            if remaining_change <= 0:
                break
            # Максимальное количество номиналов на сдачу
            max_nodes = min(remaining_change // nominal, temp_bank[nominal])

            if max_nodes > 0:
                change_nodes[nominal] = max_nodes
                remaining_change -= max_nodes * nominal
                temp_bank[nominal] -= max_nodes

        # Проверяем удалось ли выдать сдачу
        if remaining_change == 0:
            # Выводим информацию о сдаче
            print(f"Сдача: {change_amount} руб.: ", end='')
            nodes_list = [f"{notes} x {nominal} руб." for nominal, notes in  change_nodes.items()]
            print(", ".join(nodes_list), end='')
            print()

            # Обновляем банк машины
            for nominal, count in change_nodes.items():
                self.bank[str(nominal)] -= count

            # Обновляем общую сумму в банке
            self.bank_sum = sum([int(nominal) * count for nominal, count in self.bank.items()])
            return True
        else:
            print(f"Извините, не могу выдать сдачу {change_amount} руб. доступными купюрами")
            return False


    def change_resources(self, type_coffee, coffee_volume):
        """Уменьшает ресурс кофе после выдачи заказа"""
        self.menu[type_coffee]['resources'] -= coffee_volume


    def run(self, type_coffee, coffee_volume):
        """Метод имитации работы кофемашины"""

        print("Заказ принят!")
        print("Вжжж-тррр-тррр...")
        print("Пшшшшшш...")
        print("Гррр-гррр-вжжж...")
        print("Пш-ш-ш-ш...")
        print("Пауза....")
        print("Дзынь!")
        print("Ваш кофе готов. Заберите напиток.")

        # Изменяем остаток кофе
        self.change_resources(type_coffee, coffee_volume)


    def get_many(self):
        """Метод оплаты, получает от пользователя кеш,
        проверяет достаточно ли пользователь внес
        купюр и проверяет, может ли он сдать сдачи"""
        # Переменная хранит внесенные пользователем деньги
        user_bank = 0
        while True:

            get_cash = int(input("Вставьте купюру для отплаты: "))
            # Переменная хранит внесенные пользователем деньги
            user_bank += get_cash

            if user_bank < self._user_debt:
                print(f"Доплатите еще {self._user_debt - user_bank}")
            elif user_bank == self._user_debt:
                # Готовим кофе
                self.run(self._user_coffe, self._user_coffee_volume)
                break
            elif user_bank > self._user_debt:
                change_amount = user_bank - self._user_debt
                # Если в кофе машине есть деньги, выдадим сдачу
                if self.calculate_change(change_amount):
                    # Готовим кофе
                    self.run(self._user_coffe, self._user_coffee_volume)
                    break
                else:
                    print(f"Извините, в машине недостаточно купюр для сдачи {change_amount} руб.")
                    print(f"Пожалуйста, внесите точную сумму {self._user_debt} руб.")
                    user_bank = 0  # Сбрасываем внесенную сумму
                    continue





user = CoffeeMachine()
user.display_menu()
user.request_order()
user.get_many()
# Тест остатка банка и объема кофемашины
print(user.menu)