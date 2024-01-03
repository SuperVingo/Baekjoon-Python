import sys
lst = [i for i in range(1, 21)]
for i in range(10):
    N, M = map(int, sys.stdin.readline().split())
    r = lst[N:M].reverse()
    lst = lst[:N] + r + lst[M:]

for i in lst:
    print(i, end=" ")