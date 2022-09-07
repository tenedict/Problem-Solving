import sys

stack = []

for _ in range(int(sys.stdin.readline())):
    word = (sys.stdin.readline().split())
    if word[0]=='push':
        stack.append(word[1])
    
    if word[0] == 'top':
        if len(stack) != 0:
            print(stack[-1])
        else:
            print(-1)
    
    if word[0] == 'size':
        print(len(stack))

    if word[0] == 'empty':
        if len(stack) == 0:
            print(1)
        else:
            print(0)
    if word[0] == 'pop':
        if len(stack) != 0:
            print(stack.pop())
        else:
            print(-1)


    
