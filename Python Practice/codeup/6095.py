n = int(input())

li =[['0' for _ in range(19)] for _ in range(19)]

for _ in range(n):
    x,y = map(int,input().split())
    li[x-1][y-1] = '1'



for i in li:
    for j in i:
        print(j,end=" ")
    print()

# for i in range(1, 20) :
#   for j in range(1, 20) : 
#     print(li[i-1][j-1], end=' ')
#   print()  