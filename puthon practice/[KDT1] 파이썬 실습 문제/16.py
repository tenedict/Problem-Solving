#16번 문제풀이
g = 0
for i in 'aaa666aaa666':
    if i == 'a':
        g +=1
    elif i == 'e':
        g +=1 
    elif i == 'i':
        g +=1 
    elif i == 'o':
        g +=1 
    elif i == 'u':
        g +=1  
    else:
        continue
print(g)
