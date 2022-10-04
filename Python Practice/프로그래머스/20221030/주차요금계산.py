# fees = input()
records = list(input().split('", "'))
records[0] = records[0].strip('["')
records[-1] = records[-1].strip('"]')
tim = []
car = []
ino = []
for i in records:
    print(i)
    ti, ca, io = i.split()
    print(ti)
