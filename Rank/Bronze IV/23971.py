import math
line = input().split()
a = int(line[0])
b = int(line[1])
c = int(line[2])
d = int(line[3])
print(int(math.ceil(a/(c+1)) * math.ceil(b/(d+1))))