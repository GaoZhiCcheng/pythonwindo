def canshu(str):# str 是个形参 给canshu传入一个指定str类型的参数
    print(str)# 显示函数的参数
canshu(str='实参')# 实参 是实参
print("-分割线-"*10)
# 不需要指定函数参数的顺序
def canshu2(age,name): # 定义hanshu2 里面有两个形参
    print('年龄；',age) # 打印形参
    print('姓名：',name)
canshu2(age = 24,name = '高志成') # 向canshu2传入两个实参并打印出来
