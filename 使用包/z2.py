def deco(func):
    def _deco(a,b):
        print('在函数myfunc（）之前被调用')
        ret = func(a,b)
        print('在函数myfunc（）之后被调用，结果是%s'%ret)
        return ret
    return _deco

@deco
def myfunc(a,b):
    print('函数myfunc(%s,%s)被调用！'%(a,b))
    return  a + b
myfunc(1,2)
myfunc(3,4)
