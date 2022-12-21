import sys
n, m = map(int,sys.stdin.readline().split())

chan = [0]*n
for i in range(n):
    chan[i] = list(map(int,sys.stdin.readline().split()))

for j in range(m):
    dap = 0
    a,b,c,d = map(int,sys.stdin.readline().split())
    for ii in range(a,c+1):
        for jj in range(b,d+1):
            dap +=chan[ii-1][jj-1]
    print(dap)