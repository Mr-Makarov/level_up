import csv, json
from django.shortcuts import render, redirect
from .forms import ConnectServerForm, ServerAddForm
from .services import run_scan
from applications import test_connection
from django.contrib.auth.decorators import login_required
from .models import ScanProfiles, Servers, ServerStatus
from django.contrib import messages
from django.http import JsonResponse


# Create your views here.
@login_required
def index(request):
    results = None
    form = ConnectServerForm()

    profiles = ScanProfiles.objects.all()
    form.fields['check'].choices = [(r.id, r.name) for r in profiles]

    # Заполнение формы если передан GET  pfghjc
    server_id = request.GET.get('server_id')
    if server_id:
        try:
            server = Servers.objects.get(id=server_id, created_by=request.user)
            initial = {
                'host': server.host,
                'port': server.port,
                'username': server.username,
                'password': server.password,
            }
            form = ConnectServerForm(initial=initial)
            form.fields['check'].choices = [(p.id, p.name) for p in profiles]
        except Servers.DoesNotExist:
            pass

    if request.method == 'POST':

        form = ConnectServerForm(request.POST)

        profiles = ScanProfiles.objects.all()
        form.fields['check'].choices = [(r.id, r.name) for r in profiles]

        if form.is_valid():
            host = form.cleaned_data['host']
            port = form.cleaned_data['port']
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            check_id = form.cleaned_data['check']
            profile = ScanProfiles.objects.get(id=check_id)
            checks = profile.checks.all()
            action = request.POST.get('action')

            if action == 'check':
                results = test_connection(host, port, username, password)
            elif action == 'scan':
                results = run_scan(host, port, username, password, checks)
            else:
                results = f"❌ Неизвестное действие: {action}"
        else:
            results = f"❌ Ошибка в форме: {form.errors}"

    return render(request, 'web_interface/index.html', {
        'form': form,
        'results': results
    })


@login_required
def servers_list(request):
    servers = Servers.objects.filter(is_active=True)
    for server in servers:
        try:
            status_obj = ServerStatus.objects.get(server=server)
            if status_obj.status == 'ok':
                server.status_icon = '✅'
                server.status_text = 'Соединение установлено'
            else:
                server.status_icon = '❌'
                server.status_text = 'Не удалось подключиться'
            server.status_tooltip = status_obj.message
        except ServerStatus.DoesNotExist:
            server.status_icon = '❓'
            server.status_tooltip = 'Не проверялось'
    return render(request, 'web_interface/servers_list.html', {'servers': servers})


@login_required
def server_add(request):
    """Представление для добавления сервера"""

    if request.method == 'POST':
        form = ServerAddForm(request.POST)
        if form.is_valid():
            server = Servers(
                name=form.cleaned_data['name'],
                host=form.cleaned_data['host'],
                port=form.cleaned_data['port'],
                username=form.cleaned_data['username'],
                password=form.cleaned_data['password'],
                is_active=form.cleaned_data['is_active'],
                created_by=request.user
            )
            server.save()
            return redirect('servers_list')
    else:
        form = ServerAddForm()

    return render(request, 'web_interface/server_form.html', {'form': form})


@login_required
def servers_import(request):
    """Представление для массового добавления серверов"""

    if request.method == 'POST' and request.FILES.get('csv_file'):
        csv_file = request.FILES['csv_file']
        # Проверяем расширение
        if not csv_file.name.endswith('.csv'):
            messages.error(request, 'Файл должен быть в формате CSV')
            return redirect('servers_list')

        # Читаем файл
        decoded = csv_file.read().decode('utf-8').splitlines()
        reader = csv.DictReader(decoded)

        added = 0
        errors = []

        for row_num, row in enumerate(reader, start=2):
            try:
                # Создаём сервер
                server = Servers(
                    name=row['name'],
                    host=row['host'],
                    port=int(row.get('port', 22)),
                    username=row['username'],
                    password=row['password'],
                    is_active=row.get('is_active', 'True').lower() == 'true',
                    created_by=request.user
                )
                server.save()
                added += 1
            except Exception as e:
                errors.append(f"Строка {row_num}: {str(e)}")

        # Сообщения пользователю
        if added:
            messages.success(request, f'Добавлено серверов: {added}')
        if errors:
            messages.error(request, f'Ошибки: {", ".join(errors[:5])}')

        return redirect('servers_list')

    return redirect('servers_list')


@login_required
def check_connection_ajax(request):
    """Представление проверки соединения для группы серверов"""

    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            host = data.get('host')
            port = data.get('port')
            username = data.get('username')
            password = data.get('password')
            success, message = test_connection(host, port, username, password)
            return JsonResponse({'success': success, 'message': message})
        except Exception as e:
            return JsonResponse({'success': False, 'message': str(e)}, status=400)
    return JsonResponse({'success': False, 'message': 'Invalid request'}, status=405)


@login_required
def update_server_status(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            server_id = data.get('server_id')
            success = data.get('success')
            message = data.get('message', '')
            server = Servers.objects.get(id=server_id, created_by=request.user)
            status_obj, created = ServerStatus.objects.get_or_create(server=server)
            status_obj.status = 'ok' if success else 'error'
            status_obj.message = message
            status_obj.save()
            return JsonResponse({'success': True})
        except Servers.DoesNotExist:
            return JsonResponse({'success': False, 'error': 'Server not found'}, status=404)
        except Exception as e:
            return JsonResponse({'success': False, 'error': str(e)}, status=400)
    return JsonResponse({'success': False, 'error': 'Invalid request'}, status=405)