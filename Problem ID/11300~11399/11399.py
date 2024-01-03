import sys

N = int(sys.stdin.readline())
lst = sorted(list(map(int, sys.stdin.readline().split())))

c = 0
for i in range(N, 0, -1):
    c += (i * lst[len(lst) - i])
print(c)