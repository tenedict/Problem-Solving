n, m = map(int,input().split())

su = []

def dfs():
    if len(su) == m:
        for j in su:
            print(j,end=' ')
        print('')
        return
    
    for i in range(1,n+1):
        if i not in su:
            su.append(i)
            dfs()
            su.pop()
dfs()