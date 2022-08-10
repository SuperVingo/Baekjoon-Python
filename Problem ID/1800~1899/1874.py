import sys

n = int(input())
l = [int(sys.stdin.readline().strip()) for i in range(n)]

m = 1
i = 0
s = []
r = []
while True:
    if len(s) == 0 or s[-1] != l[i]:
        if m == n + 1:
            break
        else:
            s.append(m)
            r.append('+')
            m = m + 1
    elif s[-1] == l[i]:
        s.pop()
        r.append('-')
        i = i + 1

if len(s) == 0:
    for i in r:
        print(i)
else:
    print("NO")