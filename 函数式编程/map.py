L1 = [i for i in range(10)]
print(L1)
l2 = []
for i in L1:
    l2.append(i*10)
print(l2)

def  amap(n):
    return n * 10
l3 = map(amap,L1)

for i in  l3:

    print(i)

print(l3)
