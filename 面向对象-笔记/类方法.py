# 定义并使用类方法
# 方法的第一个参数必须是self 而且不能忽略
# 方法的调用时需要实例化类 并且 以 ‘实例名.方法名（参数列表）’ 的形式调用
# 必须整体进行一个单位的缩进，表示这个方法属于类中的内容
# 请看下列

class Smp:
    def info(self):
        print('定义的类')
    def print_info(self,x,y):
        return print('我类方法print_info .....',x+y)

s = Smp()
print('调用类方法的结果..........')
s.info() # 实例化 info 打印出他的属性
print('下面是调用实例化对象 s 中的 print_info()方法 ')
s.print_info(12,18)