from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
# Create your views here.

@csrf_exempt
def login(request):
    if request.method!='POST':
        return render(request,'login.html',{ 'error': ' ' })
    type=request.POST['type']
    if type=='student':
        try:
            user=Student.objects.get(stu_ID=request.POST['id'])
            print("aaa")
            return render(request,'login.html',{'error':'好嘛'})
        except:
            return render(request,'login.html',{'error':'妈耶'})
    elif type=='teacher':
        user=Student.objects.get(ins_ID=request.POST['id'])
    elif type=='education manager':
        user=Student.objects.get(Mana_ID=request.POST['id'])
    elif type=='system manager':
        user=Student.objects.get(sys_ID=request.POST['id'])


