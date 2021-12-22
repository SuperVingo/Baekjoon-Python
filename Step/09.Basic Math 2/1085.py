line = input().split()
x = int(line[0])
y = int(line[1])
w = int(line[2])
h = int(line[3])

width = min(x, w-x)
height = min(y, h-y)
print(min(width, height))