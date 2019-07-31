# __inlt__是一个魔法函数 直接初始类
class Asdf:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def b(self):
        return print('我叫{}，今年岁了{}'.format(self.name,self.age))
a = Asdf('gao',age = 24)
a.b()