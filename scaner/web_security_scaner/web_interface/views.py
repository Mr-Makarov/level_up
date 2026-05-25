from django.shortcuts import render
#from django.http import HttpResponse
from .forms import ConnectServerForm
from .services import run_scan
from .applications import test_connection



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





