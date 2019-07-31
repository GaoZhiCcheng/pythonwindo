# 计算元组内元素的和
def tpl_sum(t):
    result = 0
    for  i  in  t:
        result += i
    return result

print('（1.2.3.4）元素中的和为：',tpl_sum((1,2,3,4)))
print('[4567]列表中的元素和为：',tpl_sum([4,5,6,7]))