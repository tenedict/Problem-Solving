from itertools import combinations

people, p, e = map(int, input().split())

n = 0
allsaram = []
for i in range(people):
    n += 1
    saram = []
    saram.append(n)
    a, b = map(int, input().split())
    saram.append(a)
    saram.append(b)
    allsaram.append(saram)
print(allsaram)
johap = []

for j in combinations(range(people), p):
    johap.append(j)

print(johap)
realmin = -1
realmax = -1

yes = 0
yyes = 0
num = 0
nummax = 0
possiblemin = []
for k in johap:
    num += 1
    min_ = 0
    for kk in k:
        min_ += int(allsaram[kk][1])
    im = []
    im.append(num)
    im.append(min_)
    possiblemin.append(im)
    if min_ < realmin or realmin == -1:
        realmin = min_

possiblemax = []
for l in johap:
    nummax += 1
    max_ = 0
    for ll in l:
        max_ += int(allsaram[ll][2])
    im = []
    im.append(nummax)
    im.append(max_)
    possiblemax.append(im)
    if max_ > realmax or realmax == -1:
        realmax = max_
        


print(realmax, realmin)
if e <= realmax and realmin <= e:
    print(1)
    print(yes)
    print(possiblemax,possiblemin)
    for poss in possiblemax:
        if poss[1] >= e :
            if possiblemin[poss[0]-1][1] <= e:
                print(johap[poss[0]-1])
                dap = johap[poss[0]-1]
                break
    sarmin = []
    sarmax = []
    for d in dap:
        sar = allsaram[d]
        sarmin.append(sar[1])
        sarmax.append(sar[2])
    e - min(sarmin)*len(dap)
    
        
else:
    print(-1)
