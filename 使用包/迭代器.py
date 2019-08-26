# 创建一个迭代器 并使用
class User: # 定义迭代器类 User


    def __init__(self,x=2,max=50): # 定义构造方法
        self.__mul,self.__x =x,x # 初始化属性 x的初始值是2
        self.__max = max # 初始化属性


    def __iter__(self):# 定义迭代器协议方法
        return  self #返回类的自身

    def __next__(self): # 定义迭代的协议方法
        if self.__x and self.__x != 1: # 如果x的值不是1
            self.__mul *= self.__x # 设置mul 的值
            if self.__mul <= self.__max: # 入过mul 的值小于等于预设的最大值max
                return self.__mul # 则返回 mul 的值
            else:
                raise StopAsyncIteration  # 当超过参数max的值时会引发Stopasynclteration 异常
        else:
            raise StopAsyncIteration
if __name__ == '__main__':
     my = User()
     for  i  in my:
        print('迭代的数据元素为：',i)




