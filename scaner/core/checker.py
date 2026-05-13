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
        Check('N01', "egrep '^PermitRootLogin|^#PermitRootLogin' /etc/ssh/sshd_config | awk '{print $2}'", 'no', 'Запрет SSH логина root'),
    ]

    # Проверяем
    for check in checks:
        output, error, exit_code = conn.execute(check.command)

        if exit_code != 0:
            print(f"{check.code}: {error.strip()} [ ERROR ]")
        elif check.expected == output.strip():
            print(f"{check.code}: {check.description} - {check.command} (Exp: {output.strip()})  [ PASS ]")
        else:
            print(f"{check.code}: {check.description} - {check.command} (Exp: {output.strip()})  [ FAIL ]")

if __name__ == "__main__":
    main()