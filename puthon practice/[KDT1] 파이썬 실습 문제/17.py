#17번 문제풀이
g = 'banana'
for i in g:
    i = ord(i)
    i = chr(i-32)
    print(i,end='')