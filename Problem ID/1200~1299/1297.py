import math
line = input().split()
n = int(line[0])
h = int(line[1])
w = int(line[2])
a = math.sqrt(n**2 / (h**2 + w**2))
print(int(h*a), int(w*a))