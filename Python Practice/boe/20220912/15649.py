n,m = list(map(int,input().split()))

s = []
print(s,'99t')

def dfs():
    if len(s)==m:
        print(' '.join(map(str,s)))
        return
    
    for i in range(1,n+1):
        if i not in s:
            s.append(i)
            dfs()
            s.pop()
            print('===')

dfs()
