line = input().split()
a = int(line[0])
b = int(line[1])

c = (a+b)//2
d = a - c

if(a == (c+d) and b == abs(c-d) and c >= 0 and d >= 0):
    print(max(c, d), min(c, d))
else:
    print(-1)