line = input().split()
a = int(line[0])
b = int(line[1])
x = int(line[2])
y = int(line[3])

n = abs(a-b)
u0 = abs(a-x) + abs(b-y)
u1 = abs(a-y) + abs(b-x)

print(min(n, u0, u1))