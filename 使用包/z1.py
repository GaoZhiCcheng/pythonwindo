# 定义一一个装饰器函数zz
def zz(fun):
    def wrapper(*args,**bian): # 定义一个包装器函数
        print('开始运行')
        fun(*args,**bian) # 使用被装饰器函数
        print('运行结束')
    return wrapper # 返回包装器函数 wrapper

@zz # 装饰器函数语句
def demo_decoration(x): # 定义普通函数 他被装饰器装饰

    a = [] # 定义控列表
    for  i  in  range(x): # 遍历返回x的值
        a.append(i) # 将i 添加到列表末尾
    print(a)
@zz
def hello(name): # 定义普通函数hello ，他被装饰器装饰
    print('hello',name)


if __name__ == '__main__':
    demo_decoration(5) # 调用被装饰器装饰的函数 demo_decoration
    print( )
    hello('高川') # 调用被装饰器装饰的函数hello

