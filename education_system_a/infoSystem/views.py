from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from .models import Student,Instructor,Course
from django.http import HttpResponseRedirect
from .db_manage import update_student, update_instructor, update_course
from .import import import_record
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
                                                 'href': "stu-manage",
                                                 'name':'学生账户管理'
                                              },{
                                                 'href': 'ins-manage',
                                                 'name':'教师账户管理'
                                              },{
                                                 'href': 'course-manage',
                                                 'name':'课程管理'
                                              },{
                                                 'href': '',
                                                 'name':'教务管理账户管理'
                                              }],
                                  'user': user,
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

def personal(request, user_id):
    print(request.GET)
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
                   'name':'学生账户管理',
                   'href': "stu-manage"
                },{
                   'href': 'ins-manage',
                   'name':'教师账户管理'
                },{
                   'href': 'course-manage',
                   'name':'课程管理'
                },{
                   'href': '',
                   'name':'教务管理账户管理'
                }],
    'user': Student.objects.get(stu_ID=user_id)
    })
def stu_manage(request):
    return render(request,'stu-account-manage.html',{
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
                   'name':'学生账户管理',
                   'href': "stu-manage",
                },{
                   'name':'教师账户管理',
                   'href': 'ins-manage',
                },{
                   'name':'课程管理',
                   'href': 'course-manage',
                },{
                   'name':'教务管理账户管理',
                   'href': '',
                }],
    'user': Student.objects.get(stu_ID='3150102540'),
    'students': Student.objects.all()
    })

def ins_manage(request):
    return render(request,'ins-account-manage.html',{
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
                   'name':'学生账户管理',
                   'href': "stu-manage",
                },{
                   'name':'教师账户管理',
                   'href': 'ins-manage',
                },{
                   'name':'课程管理',
                   'href': 'course-manage',
                },{
                   'name':'教务管理账户管理',
                   'href': '',
                }],
    'user': Student.objects.get(stu_ID='3150102540'),
    'instructor': Instructor.objects.all()
    })

def course_manage(request):
    return render(request,'course-manage.html',{
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
                   'name':'学生账户管理',
                   'href': "stu-manage",
                },{
                   'name':'教师账户管理',
                   'href': 'ins-manage',
                },{
                   'name':'课程管理',
                   'href': 'course-manage',
                },{
                   'name':'教务管理账户管理',
                   'href': '',
                }],
    'user': Student.objects.get(stu_ID='3150102540'),
    'course': Course.objects.all()
    })

@csrf_exempt
def update_stu(request):
    update_student(request)
    return HttpResponseRedirect('/home/stu-manage')

@csrf_exempt
def update_ins(request):
    update_instructor(request)
    return HttpResponseRedirect('/home/ins-manage')

@csrf_exempt
def update_cour(request):
    update_course(request)
    return HttpResponseRedirect('/home/course-manage')

