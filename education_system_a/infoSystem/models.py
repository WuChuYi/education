from django.db import models

# Create your models here.

class Student(models.Model):
    stu_ID = models.CharField(max_length=20, default=None, primary_key=True)
    stu_name = models.CharField(max_length=20, null=True, blank=True, default="New User")  # if None, replace by username
    stu_grade = models.CharField(max_length=10, null=True, blank=True, default=None)
    stu_gender = models.CharField(max_length=10, null=True, blank=True, default=None)  # 'M'|'F'|null
    major_ID = models.CharField(max_length=20, null=True, blank=True, default=None)
    stu_password = models.CharField(max_length=20, null=True, blank=True, default="123456")
    tot_cred = models.DecimalField(max_digits=20, decimal_places=1)
    avatar = models.ImageField(upload_to='course/cover-img/', default=None, null=True)

class Instructor(models.Model):
    ins_ID = models.CharField(max_length=20, default=None, primary_key=True)
    ins_name = models.CharField(max_length=20, null=True, blank=True, default="New User")
    ins_gender = models.CharField(max_length=10, null=True, blank=True, default=None)
    ins_password = models.CharField(max_length=20, null=True, blank=True, default="123456")
    dept_ID = models.CharField(max_length=20, null=True, blank=True, default=None)

class Course(models.Model):
    course_ID = models.CharField(max_length=20, default=None, primary_key=True)
    title = models.CharField(max_length=20, null=True, blank=True, default="New Class")
    dept_id = models.CharField(max_length=20, null=True, blank=True, default=None)
    credits = models.DecimalField(max_digits=20, decimal_places=1)
    course_capacity = models.IntegerField()
    type = models.CharField(max_length=20, null=True, blank=True, default=None)
    need_computer =  models.CharField(max_length=10, null=True, blank=True, default=None)
    period = models.IntegerField()
    exam_method = models.CharField(max_length=10, null=True, blank=True, default=None)
    description = models.CharField(max_length=50, null=True, blank=True, default=None)

class Edu_manager(models.Model):
    Mana_ID = models.CharField(max_length=20, default=None, primary_key=True)
    Mana_name = models.CharField(max_length=20, null=True, blank=True, default="New User")
    Mana_gender = models.CharField(max_length=10, null=True, blank=True, default=None)
    Mana_password = models.CharField(max_length=20, null=True, blank=True, default="123456")
    Mana_deptID = models.CharField(max_length=20, null=True, blank=True, default=None)

class Sys_manager(models.Model):
    sys_ID = models.CharField(max_length=20, default=None, primary_key=True)
    sys_name = models.CharField(max_length=20, null=True, blank=True, default="New User")
    sys_gender = models.CharField(max_length=10, null=True, blank=True, default=None)
    sys_password = models.CharField(max_length=20, null=True, blank=True, default="123456")

class Ins_course(models.Model):
    Ins_ID = models.ForeignKey('Instructor', on_delete=models.SET_NULL, null=True)
    Course_ID = models.ForeignKey('Course', on_delete=models.SET_NULL, null=True)

