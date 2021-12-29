import math
line = input().split()
a = int(line[0])
b = int(line[1])
print(math.ceil(b / abs(a-b)))