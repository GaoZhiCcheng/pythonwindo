import  module.hello  as u# 调用包 module里面的文件 hello

u.helo() # 调用包module 里面的文件 hello文件的里面的一个函数
from module import  hello # 第二种调用方式

hello.helo() # 第二种调用方法


from module.hello import helo  # 直接调用包文件里面的一个函数
helo()