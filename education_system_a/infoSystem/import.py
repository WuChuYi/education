#!/usr/bin/env python
import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "education_system_a.settings")

def import_record(f):
    from .models import Instructor

    recordList = []
    for line in f:
        print(line)
        parts = line.split(' ')
        recordList.append(Instructor(ins_ID=parts[0], ins_name=parts[1], ins_gender=parts[2], dept_ID=parts[4]))

    f.close()

    # 以上四行 也可以用 列表解析 写成下面这样
    # BlogList = [Blog(title=line.split('****')[0], content=line.split('****')[1]) for line in f]

    Instructor.objects.bulk_create(recordList)