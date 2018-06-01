
from django.urls import path
from . import views

app_name = 'infoSystem'

urlpatterns = [
    path('', views.login, name='login'),
    path('personal/<int:user_id>',views.personal, name='personal'),
    path('stu-manage', views.stu_manage, name='stu_manage'),
    path('ins-manage', views.ins_manage, name='ins_manage'),
    path('course-manage', views.course_manage, name='course_manage'),
    path('update-stu',views.update_stu, name='update_stu'),
    path('update-ins', views.update_ins, name='update_ins'),
    path('update-cour',views.update_cour, name='update_cour'),
]
