""""
Модуль для запуска сканирования
"""
from core.ssh_client import SSHConnection
from core.checker import  main


def run_scaner(host: str, port: int, user: str, passwd: str):
    """Функция запуска сканирования"""

    results = []

    # Подключаемся к серверу
    conn = SSHConnection()
    conn.connect(host, port, user, passwd)

    # Проверяем
    for check in main():
        output, error, exit_code = conn.execute(check.command)

        # Получаем статус
        if exit_code != 0:
            status = 'ERROR'
        elif check.expected == output.strip():
            status = 'PASS'
        else:
            status = 'FAIL'
        # Записываем результат
        results.append({
            'code': check.code,
            'description': check.description,
            'verifiable_value': check.output,
            'status': status,
            'expected': check.expected,
            'current': output.strip()
        })
    return results




