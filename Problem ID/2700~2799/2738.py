a = []
b = []
c = []

line = input().split()
n = int(line[0])
m = int(line[1])
for i in range(n):
    a.append(list(map(int, input().split())))
for i in range(n):
    b.append(list(map(int, input().split())))

for i in range(n):
    t = []
    for j in range(m):
        t.append(a[i][j] + b[i][j])
    c.append(t)

for i in range(n):
    for j in range(m):
        print(c[i][j], end=' ')
    print()