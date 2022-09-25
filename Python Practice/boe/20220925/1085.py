x,y,w,h = map(int,input().split())
print(min(min(x,int(w-x)),min(y,int(h-y))))