# 类的属性 self 相当于 一个房子的门
class Boll:
    def ast(self,name):
        self.name = name
    def bs(self):
        print('hello {0},我是一个球，你要一起玩吗'.format(self.name))
# 实例化
b = Boll()
b.ast('xiaopang')
c = Boll()
c.ast('dapang')
b.bs()
c.bs()