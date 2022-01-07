line = input().split()
n = int(line[0])
m = int(line[1])
k = int(line[2])

o = m
x = n-m

of = k
xf = n-k

print(min(o, of) + min(x, xf))
