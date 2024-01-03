import sys
import heapq

N = int(sys.stdin.readline())

lst = []
for i in range(N):
    l = int(sys.stdin.readline())
    if l == 0:
        if len(lst) == 0:
            print(0)
        else:
            print(heapq.heappop(lst))
    else:
        heapq.heappush(lst, l)