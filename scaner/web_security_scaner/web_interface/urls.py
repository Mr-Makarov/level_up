from django.urls import path
from . import views



urlpatterns = [
    path('', views.index, name='index'),
    path('servers/', views.servers_list, name='servers_list'),
    path('servers/add/', views.server_add, name='server_add'),
    path('servers/import/', views.servers_import, name='servers_import'),
]
