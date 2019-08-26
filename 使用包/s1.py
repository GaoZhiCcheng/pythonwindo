# 生成器
def  fib(max):
    a,b = 1,1
    while a < max:
        yield a

        a,b = b,a+b


for  i  in  fib(15):
    print(i)
