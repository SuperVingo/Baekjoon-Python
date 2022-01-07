line = input().split()
m = int(line[0])
s = int(line[1])
g = int(line[2])
line = input().split()
a = float(line[0])
b = float(line[1])
line = input().split()
l = int(line[0])
r = int(line[1])

wl = l / a
wr = r / b
tl = m / g
tr = m / s
if(wl + tl > wr + tr):
    print('latmask')
else:
    print('friskus')
