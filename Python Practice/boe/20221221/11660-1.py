import sys
n, m = map(int,sys.stdin.readline().split())

chan = [0]*n
for k in range(n):
    chan[k] = list(map(int,sys.stdin.readline().split()))

sum_chan = [[0 for _ in range(n+1)] for _ in range(n+1)]
for i in range(1,n+1):
    for j in range(1,n+1):
        sum_chan[i][j] = chan[i-1][j-1] + (sum_chan[i-1][j]) + (sum_chan[i][j-1]) - (sum_chan[i-1][j-1])

for j in range(m):

    a,b,c,d = map(int,sys.stdin.readline().split())
    print(sum_chan[a-1][b-1]-sum_chan[a-1][d]-sum_chan[c][b-1]+sum_chan[c][d])