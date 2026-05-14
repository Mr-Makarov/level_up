"""
Чекер, осуществляет проверку безопасности
"""

from  ssh_client import SSHConnection


class Check:
    """Класс проверки одного параметра безопасности"""
    def __init__(self, code: str, command: str, expected: str,  description=""):
        """Инициализация класса проверки"""
        self.code = code
        self.command = command
        self.expected = expected
        self.description = description


def main():
    """Главная функция, запускает проверку"""
    # Подключаемся к серверу
    conn = SSHConnection()
    conn.connect('127.0.0.1', 2221, 'ansible', '!QAZxsw2')

    # Список проверок (базовый профиль)
    checks = [
        Check('K01', 'sysctl -n net.ipv4.tcp_syncookies', '1', 'Защита от SYN-флуда'),
        Check('K02', 'sysctl -n fs.suid_dumpable', '0', 'Ограничение core dump'),
        Check('K03', 'sysctl -n kernel.kptr_restrict', '1', 'Ограничение доступа к символам ядра'),
        Check('K04', 'sysctl -n kernel.randomize_va_space', '1', 'Полная ASLR'),
        Check('K05', 'sysctl -n kernel.dmesg_restrict', '1', 'Только root может читать dmesg'),
        Check('N01', "egrep '^PermitRootLogin|^#PermitRootLogin' /etc/ssh/sshd_config | awk '{print $2}'", 'no', 'Запрет SSH логина root'),
        Check('F01', "stat -L -c '%a' /var/mail", '755', 'Установить корректные права доступа к /var/mail'),
        Check('F02', "for dir in /home/*; do [ \"$(stat -c '%a' \"$dir\")\" != \"700\" ] && echo 'FAIL'; done | head -1",
              "", # Ожидаем пустой вывод 
              'Все домашние каталоги имеют права 700'),
    ]

    # Проверяем
    for check in checks:
        output, error, exit_code = conn.execute(check.command)

        if exit_code != 0:
            print(f"{check.code}: {error.strip()} [ ERROR ] ❌")
        elif check.expected == output.strip():
            print(f"{check.code}: {check.description} - {check.command} (Exp: {output.strip()})  [ PASS ] ✅")
        else:
            print(f"{check.code}: {check.description} - {check.command} (Exp: {output.strip()})  [ FAIL ] ⚠️")

if __name__ == "__main__":
    main()