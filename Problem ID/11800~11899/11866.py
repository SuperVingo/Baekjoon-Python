n, k = map(int, input().split())

s = [i for i in range(1, n+1)]
l = []
i = 0
while len(s) != 0:
    if(len(s) != 0):
        i = (i + (k - 1)) % len(s)
    l.append(s[i])
    del s[i]
    
print("<", end='')
for i in l[:-1]:
    print(i, end=', ')
print(l[-1], end='>')