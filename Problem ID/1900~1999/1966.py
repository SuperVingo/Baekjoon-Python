import sys
from collections import deque

test = int(input())

for i in range(test):
    n, m = map(int, sys.stdin.readline().strip().split())
    l = deque(map(int, sys.stdin.readline().strip().split()))
    t = deque([False if i != m else True for i in range(n)])
    p = 0

    while True:
        if l[0] == max(l): # print
            p = p + 1
            if t[0]:
                break
            l.popleft(), t.popleft()
        else:
            l.append(l.popleft()), t.append(t.popleft())
    print(p)