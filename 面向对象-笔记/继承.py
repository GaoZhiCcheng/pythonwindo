# 在python中子类是可以继承父类的所有属性 请看下列
class Psor: # 创建一个父类
    def far(self):
        print("正在调用父类..........")
# 建立子类

class A(Psor):
    def erzi(self):
        print("我是子类 我已经继承了父类的属性......")
# 实例化父类
c =  Psor()
# 调用父类
c.far()
# 实例化子类
b = A()
# 调用子类 此时 子类拥有父类的属性
b.far()
b.erzi()
# 同时也可以进行多重继承 请看下列


# 创建三个父类 进行多重继承
class A:
    def sd(self):
        print('我继承 1 .........')
class B:
    def asd(self):
        print('我是继承 2')
class C:
    def  bsd(self):
        print("我是继承3")


# 建立子类 继承上面三个父类
class D(A,B,C):
    def zilei(self):
        print('我是子类 我有三个父类')



# 此时 子类可以调用以上三个父类的属性
d = D()
d.zilei()
d.asd()
d.bsd()
d.sd()
