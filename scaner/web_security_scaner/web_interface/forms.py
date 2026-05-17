from django import forms


class ConnectServerForm(forms.Form):
    """Класс для ввода данных для подключению к серверу"""

    host = forms.CharField(max_length=15, label='IP-адрес')
    port = forms.IntegerField(initial=22, label='SSH порт')
    username = forms.CharField(max_length=15, label='Логин')
    password = forms.CharField(widget=forms.PasswordInput, label='Пароль')