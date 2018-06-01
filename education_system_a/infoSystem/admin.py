from django.contrib import admin

# Register your models here.
from .models import Student, Instructor, Course, Edu_manager, Sys_manager, Ins_course, Blacklist
admin.site.register(Student)
admin.site.register(Instructor)
admin.site.register(Course)
admin.site.register(Edu_manager)
admin.site.register(Sys_manager)
admin.site.register(Ins_course)
admin.site.register(Blacklist)