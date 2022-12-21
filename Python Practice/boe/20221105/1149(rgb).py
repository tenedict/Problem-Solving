a = int(input())
price = []
for i in range(a):
    r,g,b = map(int,input().split())
    price.append([r,g,b])

for i in range(1, a):
    price[i][0] += min(price[i-1][1], price[i-1][2])
    price[i][1] += min(price[i-1][0], price[i-1][2])
    price[i][2] += min(price[i-1][0], price[i-1][1])
print(min(price[-1]))

