from django.shortcuts import render
#from django.http import HttpResponse
from .forms import ConnectServerForm
from core.ssh_client import SSHConnection
from run_cheker import run_scaner


# Create your views here.
def index(request):
    results = None
    form = ConnectServerForm()

    if request.method == 'POST':

        form = ConnectServerForm(request.POST)

        if form.is_valid():
            host = form.cleaned_data['host']
            port = form.cleaned_data['port']
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']

            action = request.POST.get('action')

            if action == 'check':
                results = test_connection(host, port, username, password)
            elif action == 'scan':
                results = run_scan(host, port, username, password)
            else:
                results = f"❌ Неизвестное действие: {action}"
        else:
            results = f"❌ Ошибка в форме: {form.errors}"


    return render(request, 'web_interface/index.html', {
        'form': form,
        'results': results
    })


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


def run_scan(host, port, username, password):
    """
    Запуск сканирования
    """
    scan_results = run_scaner(host, port, username, password)

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
