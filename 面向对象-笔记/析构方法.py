# 在python中析构方法是__del__，del前后分别有两条下划线，当时用del方法删除对象时 会调用它本身的析构函数
# 请看下例
class New:
    num_count = 0  # 所有实例都公有此变量，不能为单独每个实例分配
    def __init__(self,name):
        self.name = name
        New.num_count += 1  # 设置变量 num_count 值加1
        print(name,New.num_count)
    def __del__(self): # 定义析构方法 del
        New.num_count -= 1 # 变量num_count的值减1
        print("Del",self.name,New.num_count)
    def test():
        print('aa')


aa = New('hello')
bb = New('world')  # 进行实例化 三个对象
cc = New('aaaa')
'''
del aa
del bb
del cc   # 调用析构方法
'''
print('over')
