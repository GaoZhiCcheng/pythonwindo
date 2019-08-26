# 显示迭代器中的数据元素
class  Counter:
    def __init__(self,x=0):
        self.x = x
counter = Counter()
def used_iter():
    counter.x += 2
    return counter.x
for  i   in iter(used_iter,14):
    print('当前遍历的值时：',i)

print('------------------'*3)
