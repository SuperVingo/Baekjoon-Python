line = input().split()
bx = int(line[0])
by = int(line[1])
line = input().split()
dx = int(line[0])
dy = int(line[1])
line = input().split()
jx = int(line[0])
jy = int(line[1])

b = max(abs(jx-bx), abs(jy-by))
d = abs(jx-dx) + abs(jy-dy)
if(b < d):
    print('bessie')
elif(b > d):
    print('daisy')
else:
    print('tie')