# 拾遗
class Wugui:
    def __init__(self,x):
        self.num = x
        print('我是小乌龟')
class Xiaoyu:
    def __init__(self,x):
        self.num = x
        print('我是一条小鱼儿')
class Shuici:
    def xd(self,x,y):
        print('我是水池........')
        self.wugui = Wugui(x)
        self.xiaoyu =Xiaoyu(y)
    def print_num(self):
        print('水池里面有 %d 条小鱼 %d 只乌龟'%(self.wugui.num,self.xiaoyu.num))


s = Shuici()
s.xd(10,20)
s.print_num()