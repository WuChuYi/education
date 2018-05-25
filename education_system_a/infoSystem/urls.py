
from django.urls import path
from . import views

app_name = 'infoSystem'

urlpatterns = [
    path('', views.login, name='login'),
]
