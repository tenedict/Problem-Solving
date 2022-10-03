n = int(input())

k =[]
j = []
kj = []
for i in range(6):
    x,y = map(int,input().split())
    if x== 2 or x == 1:
        k.append(y)
        kj.append(y)
    elif x==3 or x == 4:
        j.append(y)
        kj.append(y)

k.sort()
j.sort()


a = k[2]*j[2]

if kj[0]*kj[1] == a:
    ans = a - kj[3]*kj[4]

elif kj[3]*kj[4] == a:
    ans = kj[3]*kj[4] - kj[0]*kj[1]

else:
    ans = kj[0]*kj[1] + kj[3]*kj[4]

print(ans*n)