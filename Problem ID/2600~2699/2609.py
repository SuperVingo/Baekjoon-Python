n = input().split()
a = int(n[0])
b = int(n[1])
M = max(a, b)
m = min(a, b)
gcd = 0
while True:
    if(M % m == 0):
        print(m)
        gcd = m
        break
    t = m
    m = M % m
    M = t
print((a*b)//gcd)