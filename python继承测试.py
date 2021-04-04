#!/usr/bin/env python
# _*_coding: utf-8 _*_
# @Time : 2021/4/4 11:56
# @Author : CN-JackZhang
# @File: python继承测试.py
'''继承测试'''

class father:
    def __init__(self,name,age,gender,address,enterprise):
        self.name = name
        self.age = age
        self.gender = gender
        self.address = address
        self.enterprise = enterprise
    def work_hours(self,work_place):
        hours = 0
        for i in range(365):
            if work_place == 'shenzhen':
                hours += 11
            else:
                hours += 10
        return hours

father_test = father('jack',24,'male','shenzhen','tencent')
father_work_hours = father_test.work_hours('shenzhen')
print(father_work_hours)

#开始继承
class son(father):
    pass

son_test = son('baby',5,'male','American','micsoft')
son_work_hours = son_test.work_hours('micsoft')
print(son_work_hours)






