n, m = map(int,input().split())
list_ = []
for i in range(n):
    list_.append(int(input()))

list_.sort()
mini = list_[0]
ans = mini+1
for i in range(mini):
    ans = ans -1
    su = 0
    for j in list_:
        su += j//ans
    if su == m:
        break
print(ans)