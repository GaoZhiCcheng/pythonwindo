class Use:

    def __init__(self,x=2,max=50):
        self.__mul,self.__x = x,x
        self.__max = max

    def __iter__(self):
        return self

    def __next__(self):
        if self.__x and self.__x != 1:
            self.__mul *= self.__x
            if self.__mul <= self.__max:
                return self.__mul
            else:
                raise StopIteration
        else:
            raise StopIteration

if __name__ == '__main__':
    my = Use()
    for i in my:
        print('迭代的数据元素为：',i)
