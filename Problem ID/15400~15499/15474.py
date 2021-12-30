import math
line = input().split()
a = int(line[0])
b = int(line[1])
c = int(line[2])
d = int(line[3])
e = int(line[4])

ta = math.ceil(a/b)
tb = math.ceil(a/d)
print(min(int(ta*c), int(tb*e)))