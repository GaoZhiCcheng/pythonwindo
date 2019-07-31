# 创建一个类 小狗狗 拥有 神舌头 和汪汪叫的功能
class Dog:
    def __init__(self,name,age): # 给小狗添加名字和年龄
        self.name = name
        self.age = age
    def jiesao(self): # 小狗的自我介绍
        print('我是小胖妹家的小狗%s，今年%s岁了'%(self.name,self.age))
    def wang(self):
        '''模拟狗狗汪汪叫'''
        print(self.name.title() + '正在汪汪汪..')
    def shen(self):
        print(self.name.title() + '正在伸舌头.....')
d = Dog('小胖妹',12)
d.jiesao()
d.wang()
d.shen()