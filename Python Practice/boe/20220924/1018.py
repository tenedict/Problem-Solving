a,b = map(int,input().split())
li = [list(input()) for i in range(a)]

allcnt = []
for x1 in range(b-8+1):
    for y1 in range(a-8+1):
        cnt = 0
        cnt1 = 0
        for j in range(8):
            for jj in range(8):
                # s = li[x1+j][y1+jj]
                s = (x1+j+y1+jj)

                if s%2 == 0:
                    
                    if li[y1+jj][x1+j] != 'B':
                        cnt += 1
                elif s%2 == 1:
                    if li[y1+jj][x1+j] != 'W':
                        cnt += 1

                if s%2 == 0:
                    if li[y1+jj][x1+j] != 'W':
                        cnt1 += 1
                elif s%2 == 1:
                    if li[y1+jj][x1+j] != 'B':
                        cnt1 += 1
        
        if cnt > cnt1:
            allcnt.append(cnt1)
        else:
            allcnt.append(cnt)
            




print(min(allcnt))

                        
            

