# 没有隐含调用参数，类方法与静态方法的定义方式都与实例方法不同。
# 他们的调用方式也不同，在定义静态方法是应该使用修饰符@staticmethod，进行修饰并且默认没有参数
# 在调用类方法和静态方法时，可以直接由类名进行过调用，调用前无需实例化类，也可以使用该类的任何一个实例进行调用
# 参考下列
class Jing:
    def __init__(self,x=0):
        self.x = x
    @staticmethod # 使用静态方法装饰器
    def stati_method():
        print('此处调用了静态方法')
##       print(self.x)

    @classmethod # 使用类方法装饰器
    def class_method(cls): # 定义类方法 默认参数是cls
        print('此处调用了类方法')

Jing.stati_method() # 此处调用了 静态方法

Jing.class_method() # 此处调用了 类方法

j = Jing() # 实例化类
j.class_method() # 通过实例调用类方法

j.stati_method() # 通过实例调用静态方法
