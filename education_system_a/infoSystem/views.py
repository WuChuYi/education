from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from .models import Student
# Create your views here.

@csrf_exempt
def login(request):
    if request.method!='POST':
        return render(request,'login.html',{ 'error': ' ' })
    type=request.POST['type']
    if type=='student':
        try:
            user=Student.objects.get(stu_ID=request.POST['id'])
            if user.stu_password == request.POST['code']:
                return render(request,'main.html',{
                                  'tabs': [{
                                             'href': '',
                                             'name': '主页',
                                             'icon': 'home'
                                          },{
                                              'href': '',
                                              'name': '排课系统',
                                              'icon': 'layers'
                                          },{
                                              'href': '',
                                              'name': '选课系统',
                                              'icon': 'shopping-cart'
                                          },{
                                              'href': '',
                                              'name': '校内论坛',
                                              'icon': 'users'
                                          }],
                                  'functions':[{
                                                 'name':'学生账户管理'
                                              },{
                                                 'name':'教师账户管理'
                                              },{
                                                 'name':'课程管理'
                                              },{
                                                 'name':'教务管理账户管理'
                                              }],
                                  'user': user
                                  })
            return render(request,'login.html',{'error':''})
        except:
            return render(request,'login.html',{'error':''})
    elif type=='teacher':
        user=Student.objects.get(ins_ID=request.POST['id'])
    elif type=='education manager':
        user=Student.objects.get(Mana_ID=request.POST['id'])
    elif type=='system manager':
        user=Student.objects.get(sys_ID=request.POST['id'])

def home(request):
    return render(request,'home.html',{
    'tabs': [{
                'href': '',
                'name': '主页',
                'icon': 'home'
            },{
                'href': '',
                'name': '排课系统',
                'icon': 'layers'
            },{
                'href': '',
                'name': '选课系统',
                'icon': 'shopping-cart'
            },{
                'href': '',
                'name': '校内论坛',
                'icon': 'users'
            }]
    })

def kcb(request):
    return render(request,'main.html',{
    'tabs': [{
               'href': '',
               'name': '主页',
               'icon': 'home'
            },{
                'href': '',
                'name': '排课系统',
                'icon': 'layers'
            },{
                'href': '',
                'name': '选课系统',
                'icon': 'shopping-cart'
            },{
                'href': '',
                'name': '校内论坛',
                'icon': 'users'
            }],
    'functions':[{
                   'name':'学生账户管理'
                },{
                   'name':'教师账户管理'
                },{
                   'name':'课程管理'
                },{
                   'name':'教务管理账户管理'
                }]
    })
def personal(request):
    return render(request,'personal-info.html',{
    'tabs': [{
               'href': '',
               'name': '主页',
               'icon': 'home'
            },{
                'href': '',
                'name': '排课系统',
                'icon': 'layers'
            },{
                'href': '',
                'name': '选课系统',
                'icon': 'shopping-cart'
            },{
                'href': '',
                'name': '校内论坛',
                'icon': 'users'
            }],
    'functions':[{
                   'name':'学生账户管理'
                },{
                   'name':'教师账户管理'
                },{
                   'name':'课程管理'
                },{
                   'name':'教务管理账户管理'
                }],
    'student': Student.objects.get(stu_ID='3150102540')
    })

