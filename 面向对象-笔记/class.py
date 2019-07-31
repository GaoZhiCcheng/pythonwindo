# 定义一个类
class Myclass:
    '这是一个类'
m =  Myclass() # 实例化类
print('输出类的说明')# 显示文本信息
print(m.__doc__)
print('显示类的帮助信息')
s = help(m)
print(s)
