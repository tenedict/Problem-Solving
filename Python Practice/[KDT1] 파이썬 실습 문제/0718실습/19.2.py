
n = input()
n = int(n)
t= 0
while n > 10:
    n = n/10
    t += 1
     
    if n < 10:
        print(t+1)