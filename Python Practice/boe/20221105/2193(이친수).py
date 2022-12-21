a = int(input())

li = [1,1,2]

for i in range(87):
    li.append(li[i+1]+li[i+2])

print(li[a-1])

