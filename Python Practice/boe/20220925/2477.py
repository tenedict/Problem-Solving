a = int(input())

k =[]
j = []
kj = []
for i in range(6):
    x,y = map(int,input().split())
    if x== 1 or x == 2:
        k.append(y)
        kj.append(y)
    elif x==3 or x == 4:
        j.append(y)
        kj.append(y)

k.sort()
j.sort()
s1 = kj[0]*kj[1]
s2 = kj[3]*kj[4]
print(k,j)
print(kj)
if s1 == k[2]*j[2]:
    s = s1 - s2
else:
    s = s1 + s2

print(s*a)
