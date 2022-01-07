line = input().split('/')
k = int(line[0])
d = int(line[1])
a = int(line[2])
if(d == 0 or k + a < d):
    print('hasu')
else:
    print('gosu')