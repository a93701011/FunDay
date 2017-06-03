# -*- coding: utf-8 -*-
"""
Created on Fri May 26 16:10:54 2017

@author: a93701011
"""
# install database opne source package
# pip install peewee
# https://github.com/coleifer/peewee

#! usr/bin/env python3

from peewee import *


db = SqliteDatabase("students.db")

class Student(Model):
    username = CharField(max_length = 255, unique = True)
    points = IntegerField(default = 0)
    
    class Meta:
        database = db

        
students =[
    {"username" : "KarenGu"
    ,"points" : 35353},
    {"username" :"NingCheng"
    ,"points" : 35354}
    
]

def add_student():
    for student in students:
        try:
            Student.create(username = student["username"]
                           ,points = student["points"]
                          )
        except:
            Student_instance = Student.get(username = student["username"])
            Student_instance.points = student["points"]
            Student_instance.save()
            
def top_student():
    records = Student.select().order_by(Student.points.desc()).get()
    
    return records
        
if __name__ == "__main__":
    db.connect()
    db.create_tables([Student], safe = True)
    add_student()
    print("{0.username}: {0.points}".format(top_student()))