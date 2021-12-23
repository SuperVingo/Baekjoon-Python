import math
line = input().split()
r = int(line[0])
c = int(line[1])
n = int(line[2])
print(int(math.ceil(r/n) * math.ceil(c/n)))