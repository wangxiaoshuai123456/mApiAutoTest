import calendar

import sys
import time
from importlib import reload

import baseApi
from baseApi import *
from iptv_package.runoob1 import runoob1
from iptv_package.runoob2 import runoob2
import builtins
from person import *
from student import Student

import MySQLdb

if __name__ == '__main__':

    # 类私有方法，私有属性
    stu = Student('wangxiao', 29)
    sorce = stu.getsource()
    addr= stu.getaddr()
    print(stu._Student__score)
    print(stu._addr)

    # 类Student
    print('类Student.num=', Student.num)
    stu1 = Student('xiaohua', 18)
    print('类Student.num=', Student.num)
    stu2 = Student('dali', 12)
    print('类Student.num=', Student.num)
    stu3 = Student('snashan', 20)
    print('类Student.num=', Student.num)
    stu1.displayInfo()
    stu2.displayInfo()
    stu3.displayInfo()
    print(stu1.__str__())
    print(stu2.__str__())
    print(stu3.__str__())



    # 类person
    print("person.__doc__:", Person.__doc__)
    print("person.__name__:", Person.__name__)
    print("person.__module__:", Person.__module__)
    print("person.__bases__:", Person.__bases__)
    print("person.__dict__:", Person.__dict__)

    print('person.salary=', Person.salary)
    person1 = Person('wangxiaoshuai', 18)
    person2 = Person('zhangsan', 20)
    person3 = Person('lisi', 12)
    print('person.salary=', Person.salary)
    print(person1.displayInfo())
    print(person2.displayInfo())
    print(person3.displayInfo())
    person1.addr = 'beijing'
    person2.sex = 'man'
    person1.addr = 'shanghai'
    person2.sex = 'woman'
    # del person1.addr
    # del person2.sex
    if hasattr(person1, 'addr'):
        print('has addr')
        print('addr=', getattr(person1, 'addr'))
        delattr(person1, 'addr')
    else:
        print('no has addr')

    if hasattr(person1, 'addr'):
        print('has addr')
    else:
        setattr(person1, 'addr', 'taiwan')
        print('setattr person1, addr OK')
        print('addr=', getattr(person1, 'addr'))




    # 自定义异常
    # my_exception(0)

    #FileIO
    # dir_motify('my_test_dir1')
    # # file_rw()
    # file_rename('1.xls', '111.xls')
    # file_remove('2.xls')
    print('----------------------------------------------')
    #IO
    username = input('请输出用户名:')
    print(username)
    userpwd = input('请输出密码:')
    print(userpwd)
    if username == 'admin' and userpwd == '123456':
        print('认证成功,欢迎:', username)
    print('----------------------------------------------')
    # 导包
    runoob1()
    runoob2()
    print('----------------------------------------------')

    reload(baseApi)

    print(sys.path)

    # dir
    content = dir(baseApi)
    print(content)
    print(content[5])

    # return
    sum(10, 20)
    print('函数外total=', baseApi.total)
    print('函数外total=', total)

    # lambda表达式，匿名函数
    print('3 + 2 = ', m_sum(3, 2))
    print('6 + 4 = ', m_sum(6, 4))

    # 可变参数
    printInfo_scale('wangxiaoshui')
    printInfo_scale('wangxiaoshui', 10, 20, 50, 90)

    # 默认参数
    printInfo_default('xiaohua', 10)
    printInfo_default('xiaohua')

    # 关键字参数，传入的参数顺序可变
    printInfo('wangxiaoshuai', 18)
    printInfo(age=100, name='lishuai')

    # 不可变对象的传递
    a = 5;
    immutable_trans(a)
    print('函数外a=:', a)
    # 可变对象的传递
    nums = [111, 222, 333]
    mutable_trans(nums)
    print('函数外nums=:', nums)
    for num in nums:
        if str(type(num)) == "<class 'list'>":
            print(num)
            for x in num:
                print(x)

    print('----------------------------------------------')
    # time
    print(time.asctime(time.localtime(time.time())))
    print(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))
    print(time.localtime())
    print(calendar.month(2022, 3))
    # print(time.clock())

    print('----------------------------------------------')
    devicesInfo = {'name': 'admin', 'pwd': '123456', (123, 234, 345): 'ABC', 111: '222', 1.23: 100, ('wsp',): 'aowini'}
    print(devicesInfo)
    print('str(devicesInfo): ', str(devicesInfo))
    print('len(devicesInfo): ', len(devicesInfo))

    print('----------------------------------------------')

    print(devicesInfo.keys())
    dev_keys = devicesInfo.keys()
    for key in dev_keys:
        print(key)

    print('----------------------------------------------')

    print(devicesInfo.values())
    dev_values = devicesInfo.values()
    for value in dev_values:
        print(value)

    print('----------------------------------------------')

    print(devicesInfo.items())
    devitems = devicesInfo.items();
    print(type(devitems))

    for item in devitems:
        print(item)
