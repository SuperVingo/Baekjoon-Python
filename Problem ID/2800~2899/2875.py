st = input().split(" ")
a = int(st[0])
b = int(st[1])
c = int(st[2])

t = min(a//2, b)
rm = a - t*2
rw = b - t
while t > 0 and (rm + rw) < c:
    t -= 1
    rm += 2
    rw += 1
print(t)
