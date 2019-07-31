


class Dictclass(object):
    def  __init__(self,dict):
        self.dict = dict
    def del_dict(self,key):
        if key not in self.dict.keys():
            return 'key不在字典里面'
        else:
            self.dict.pop(key)
            return '删除成功！'

d = Dictclass({'a':11,'b':546,'c':867})
print(d.del_dict('c'))