def shengyield(n):
    while n > 0:
        print('开始生成......')
        yield  n
        print('完成一次')
        n -= 1
if __name__ == "__main":
    for i in  shengyield(4):
        print('遍历得到的值：',i)

print( )
sheng_yield =  shengyield(3)

print('已实例化生成器对象')
sheng_yield.__next__()
print('第二次调用__next__()方法')
sheng_yield.__next__()
