class Person:
    """普通人类"""
    salary = 0

    def __init__(self, name, age):
        self.name = name
        self.age = age
        Person.salary += 1
        print('类Person:name=%s, age=%d' % (self.name, self.age))

    def displayInfo(self):
        print('name=%s, age=%d' % (self.name, self.age))
        print('salary=', Person.salary)

