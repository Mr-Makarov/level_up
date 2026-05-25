from core.ssh_client import SSHConnection


def test_connection(host, port, username, password):
    """
    Проверка SSH подключения
    """

    conn = SSHConnection()
    try:
        conn.connect(host, port, username, password)
        # Проверяем соединение
        transport = conn.get_transport()

        if transport is not None and transport.is_active():
            return {
            'type': 'check',
            'data': f"✅ Успешное подключение к {username}@{host}:{port}"
            }
        else:
            return {
            'type': 'check',
            'data': f"❌ Ошибка подключения: {str(e)}"
            }
    except Exception as e:
        return f"Ошибка: {e}"
    finally:
        conn.close()