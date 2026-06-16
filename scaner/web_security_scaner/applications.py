from core.ssh_client import SSHConnection


def test_connection(host, port, username, password):
    """
    Проверка SSH подключения
    """
    conn = SSHConnection()
    try:
        conn.connect(host, port, username, password)
        if conn.connected:
            return {'type': 'check', 'data': f"✅ Успешное подключение к {username}@{host}:{port}"}
        else:
            return {'type': 'check', 'data': f"❌ Не удалось подключиться"}
    except Exception as e:
        return {'type': 'check', 'data': f"❌ Ошибка: {str(e)}"}
    finally:
        conn.close()
