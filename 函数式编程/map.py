L1 = [i for i in range(10)]
print(L1)
l2 = []
for i in L1:
    l2.append(i*10)
print(l2)

def  map(n):
    return n * 10
l3 = map(map,L1)

for i in  l3:
    print(i)


