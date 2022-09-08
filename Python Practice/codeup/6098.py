import sys
li = [ sys.stdin.readline().split() for _ in range(10)]


x = 1
y = 1
li[x][y]= '9'
tf = True
while tf == True :
        if li[x][y+1] == '0':
            y += 1
            li[x][y] = '9'
            
        elif li[x+1][y] == '0':
            x += 1
            li[x][y] = '9'

        elif li[x][y+1] == '2':
            li[x][y+1] = '9'
            tf = False

        else:
            tf = False
            li[x][y]
            

for i in li:
    for j in i:
        print(j,end=' ')
    print() 
            
        