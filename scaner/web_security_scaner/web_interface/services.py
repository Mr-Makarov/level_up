from run_cheker import run_scaner


def run_scan(host, port, username, password, checks):
    """
    Запуск сканирования
    """
    scan_results = run_scaner(host, port, username, password, checks)

    # Подсчитываем статистику
    stats = {'PASS': 0, 'FAIL': 0, 'ERROR': 0}
    for item in scan_results:
        stats[item['status']] += 1

    # Возвращаем данные для отображения
    return {
        'type': 'scan',
        'data': scan_results,
        'stats': stats
    }
