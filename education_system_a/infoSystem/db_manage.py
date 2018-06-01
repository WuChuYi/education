from .models import Student,Instructor,Course,Edu_manager,Sys_manager,Ins_course

def update_student(request):
    obj = Student.objects.get(stu_ID=request.POST['id'])
    obj.stu_name = request.POST['name']
    obj.stu_gender = request.POST['gender']
    obj.stu_grade = request.POST['grade']
    obj.major_ID = request.POST['major']
    obj.save()

def update_instructor(request):
    obj = Instructor.objects.get(ins_ID=request.POST['id'])
    obj.ins_name = request.POST['name']
    obj.ins_gender = request.POST['gender']
    obj.dept_ID = request.POST['department']
    obj.save()

def update_course(request):
    obj = Course.objects.get(course_ID=request.POST['id'])
    obj.title = request.POST['title']
    obj.credits = request.POST['credit']
    obj.dept_ID = request.POST['department']
    obj.course_capacity = request.POST['capacity']
    obj.type = request.POST['type']
    obj.need_computer = request.POST['need']
    obj.period = request.POST['period']
    obj.exam_method = request.POST['exam']
    obj.description = request.POST['describe']
    obj.save()