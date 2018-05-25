from django.shortcuts import render

# Create your views here.

def login(request):
    if request.method!='POST':
        return render(request,'login.html',{})
    if type=='STUDENT':
        try:
            user=Student.objects.get(stu_ID=request.POST['name'])
            render(request,'login.html',{'error':{'msg':'好嘛'}})
        except:
            render(request,'login.html',{'error':{'msg':'妈耶'}})
    elif type=='TEACHER':
        try:
            user=Student.objects.get(ins_ID=request.POST['name'])
    elif type=='EDUCATION MANAGER':
        try:
            user=Student.objects.get(Mana_ID=request.POST['name'])
    elif type=='SYSTEM MANAGER':
        try:
            user=Student.objects.get(sys_ID=request.POST['name'])


