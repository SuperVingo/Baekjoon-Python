line = input().split()
x11 = int(line[0])
y11 = int(line[1])
x12 = int(line[2])
y12 = int(line[3])
line = input().split()
x21 = int(line[0])
y21 = int(line[1])
x22 = int(line[2])
y22 = int(line[3])
print(max(max(x11, x12, x21, x22) - min(x11, x12, x21, x22), max(y11, y12, y21, y22) - min(y11, y12, y21, y22))**2)