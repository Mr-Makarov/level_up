"""
Чекер, осуществляет проверку безопасности
"""
from web_interface.models import Checks

class Check:
    """Класс проверки одного параметра безопасности"""
    def __init__(self, code: str, command: str, expected: str, parameter_check: str, description=""):
        """Инициализация класса проверки
        """
        self.code = code
        self.command = command
        self.expected = expected
        self.parameter_check = parameter_check
        self.description = description




def get_checks_from_db():
        """Получаем данные из БД"""

        queryset = Checks.objects.all()

        # Преобразуем в список объектов твоего класса Check
        checks = []
        for db_check in queryset:
            check = Check(
                code=db_check.code,
                command=db_check.command,
                expected=db_check.expected,
                parameter_check=db_check.parameter_check,
                description=db_check.description
            )
            checks.append(check)

        return checks
        # # Список проверок (базовый профиль)
        # checks = [
        #     Check('K01', 'sysctl -n net.ipv4.tcp_syncookies', '1', 'Защита от SYN-флуда', 'net.ipv4.tcp_syncookies'),
        #     Check('K02', 'sysctl -n fs.suid_dumpable', '0', 'Ограничение core dump', 'fs.suid_dumpable'),
        #     Check('K03', 'sysctl -n kernel.kptr_restrict', '1', 'Ограничение доступа к символам ядра', 'kernel.kptr_restrict'),
        #     Check('K04', 'sysctl -n kernel.randomize_va_space', '1', 'Полная ASLR', 'kernel.randomize_va_space'),
        #     Check('K05', 'sysctl -n kernel.dmesg_restrict', '1', 'Только root может читать dmesg', 'kernel.dmesg_restrict'),
        #     Check('N01', "egrep '^PermitRootLogin|^#PermitRootLogin' /etc/ssh/sshd_config | awk '{print $2}'", 'no', 'Запрет SSH логина root', '/etc/ssh/sshd_config'),
        #     Check('F01', "stat -L -c '%a' /var/mail", '755', 'Установить корректные права доступа к /var/mail', '/var/mail'),
        #     Check('F02', "for dir in /home/*; do [ \"$(stat -c '%a' \"$dir\")\" != \"700\" ] && echo 'FAIL'; done | head -1",
        #           "", # Ожидаем пустой вывод
        #           'Все домашние каталоги имеют права 700', '/home/*'),
        # ]
        # return checks

