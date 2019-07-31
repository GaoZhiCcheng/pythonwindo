class Bass:
    def name(self,name): # 这是公有函数 所有人可见
        self.name = name
        print('%s 是大家的'%self.name)
    def __nos(self):
        print('我是私有的！')
a = Bass()
a.name("小毛毛")
a._Bass__nos()# 调用私有的方法