li = [input().split() for _ in range(19)]

n = int(input())

for i in range(n):
    x,y = map(int,input().split())
    for num in range(19):
        if num !=  x-1:   
            if li[num][y-1] == '0':
                li[num][y-1] = '1'
            elif li[num][y-1] == '1':
                li[num][y-1] = '0'
    for num in range(19):
        if num !=  y-1:   
            if li[x-1][num] == '0':
                li[x-1][num] = '1'
            elif li[x-1][num] == '1':
                li[x-1][num] = '0'


for i in li:
    for j in i:
        print(j,end=" ")
    print()