import builtins
import functools
from filecmp import cmp
from os import *

from time import sleep

import re

# 不可变对象的传递
import MySQLdb


def immutable_trans(a):
    a = 10
    print('函数内a=:', a)
    return a


# 可变对象的传递
def mutable_trans(nums):
    nums.append([1, 2, 3, 4])
    nums.append(110)
    print('函数内nums=:', nums)
    return nums


# 关键字参数，传入的参数顺序可变
def printInfo(name, age):
    print('name=', name)
    print('age=', age)


# 默认参数
def printInfo_default(name, age=100):
    print('name=', name)
    print('age=', age)


# 可变参数
def printInfo_scale(name, *vars):
    print(name)
    for var in vars:
        print(var)
    print('*******************')


total = 1


# return
def sum(x, y):
    global total
    total = x + y
    print('函数内total=', total)

    return total


# lambda表达式，匿名函数
m_sum = lambda x, y: x + y


# FILE_IO
def file_rw():
    file1 = builtins.open("data/EnCodecInfo.csv", 'r')
    contexts = file1.read(10)
    print(contexts)
    print(file1.tell())
    file1.seek(0, 0)
    contexts = file1.read(10)
    print(contexts)
    print(file1.tell())


# FILE_rename && delete
def file_rename(source_file_name, dst_file_name):
    rename(source_file_name, dst_file_name)


# FILE_rename && delete
def file_remove(file_name):
    remove(file_name)


# Dir operate
def dir_motify(new_dir_name):
    mkdir(new_dir_name)
    print(getcwd())
    chdir(new_dir_name)
    print(getcwd())
    chdir('../')
    print(getcwd())
    rmdir(new_dir_name)
    print(getcwd())


# 异常
def test_excepts(var):
    print('*******************************')
    try:
        fh = builtins.open("abs.txt", 'r', -1, 'utf-8')
        try:
            fh.write("这是一个测试文件，用于测试异常!!")
        finally:
            print("关闭文件")
            fh.close()
    except IOError as Arg:
        print("Error: 没有找到文件或读取文件失败", Arg)
    print('*******************************')
    try:
        int(var)
    except ValueError as Argu:
        print('var:值不对', Argu)
    finally:
        print('var=', var)


# 自定义异常
def my_exception(var):
    if var < 1:
        raise Exception('Invalid input argument:', var)
    else:
        print('input OK, var=', var)


# 自定义异常类
class NetWorkError(RuntimeError):
    def __init__(self, arg):
        print('arg=', arg)
        self.args = arg
        print('self.args=', self.args)


# test
class Foo(object):
    var = 1

    def foo(self):
        print('foo')

    @classmethod
    def ffoo(cls):
        print('ffoo')
        print('var=', cls.var)
        cls().foo()


# mcmp
def mcmp(x, y):
    if x[2] > y[2]:
        return 1
    elif x[2] < y[2]:
        return -1
    else:
        return 0


# sorted排序 Data eg. # L = [('john', 'A', 15), ('jane', 'B', 12), ('dave', 'B', 10)]
def m_sorted(L):
    m_list = sorted(L, key=lambda x: x[2], reverse=True)
    print(m_list)
    m_list1 = sorted(L, key=functools.cmp_to_key(mcmp), reverse=True)
    print(m_list1)


# 执行sql语句
def mysql_execute(sql):
    # 打开数据库连接
    db = MySQLdb.connect("192.168.43.123", "root", "root", "iptv", charset='utf8')
    # 使用cursor()方法获取操作游标
    cursor = db.cursor()
    try:
        # 执行sql语句
        cursor.execute(sql)
        # 提交到数据库执行

        if not re.match('select', sql):
            db.commit()
            print('受影响的行:', cursor.rowcount)
        else:
            print("select sql")
            results = cursor.fetchall()
            for row in results:
                print(row)
    except:
        # Rollback in case there is any error
        db.rollback()
    finally:
        db.close()


if __name__ == '__main__':
    # sql = "select * from userinfo_table"
    # print(re.match('adb', 'select * from userinfo_table'))

    sql_list = ('select * from userinfo_table', \
                "UPDATE EMPLOYEE SET AGE = AGE + 1 WHERE SEX = '%c'" % ('M'), \
                "DELETE FROM EMPLOYEE WHERE AGE > %s" % (20))
    for sql in sql_list:
        mysql_execute(sql)


