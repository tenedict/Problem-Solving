a,b = map(int,input().split())

li = [[0 for _ in range(b)] for _ in range(a)]


n = int(input())

for _ in range(n):
    lenth_ , way_ , x, y = map(int,input().split())
    for i in range(lenth_):
        if way_ == 0:
            li[x-1][y-1+i] = 1
        if way_ == 1:
             li[x-1+i][y-1] = 1

for _ in li:
    for __ in _:
        print(__,end=" ")
    print()