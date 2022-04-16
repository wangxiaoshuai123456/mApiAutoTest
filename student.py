from person import Person


class Student(Person):
    """学生类"""
    num = 0
    __score = 0
    _addr = '北京'

    # def __init__(self, name, age):
    #     super().__init__(name, age)
    #     print('Student: name=%s, age=%d' % (self.name, self.age))
    #     Student.num += 1

    def getNum(self):
        print('num=', Student.num)

    def __str__(self):
        return 'Student(%s, %d)' % (self.name, self.age)

    # def __getsource(self):  # 私有方法
    #     return Student.__score

    def getsource(self):  # 公有方法
        self.getaddr()
        self.getNum()
        return Student.__score

    def getaddr(self):
        return Student._addr



