
from django.urls import path
from . import views

app_name = 'infoSystem'

urlpatterns = [
    path('login/', views.login, name='login'),
    path('',views.kcb, name='kcb'),
    path('personal/',views.personal, name='personal'),
]
