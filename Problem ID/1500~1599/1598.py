line = input().split()
a = int(line[0])
b = int(line[1])
ax = (a-1) // 4
ay = (a-1) % 4
bx = (b-1) // 4
by = (b-1) % 4
print(abs(ax-bx) + abs(ay-by))