import sys
import itertools

n, m, k = map(int, input().split())
beer = []

for i in range(k):
    beer.append(list(map(int, sys.stdin.readline().split())))

johaps = itertools.combinations(beer, n)

yes = []
for johap in johaps:
    a = 0
    for i in range(n):
        a += johap[i][0]
    if a >= m:
        b = 0
        for i in range(n):
            b += johap[i][1]
            yes.append(b)
    
if yes:
    print(min(yes))
else:
    print(-1)
