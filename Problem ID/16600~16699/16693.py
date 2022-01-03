import math
line = input().split()
a1 = int(line[0])
p1 = int(line[1])
line = input().split()
r1 = int(line[0])
p2 = int(line[1])

apd = a1 / p1
rpd = ((r1**2)*math.pi) / p2
if(apd > rpd):
    print('Slice of pizza')
else:
    print('Whole pizza')