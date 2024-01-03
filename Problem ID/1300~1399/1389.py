import sys
from collections import deque

_ = sys.stdin.readline().strip().split()
N, M = int(_[0]), int(_[1])

graph = []
for _ in range(N+1):
    graph.append([])

for _ in range(M):
    _l = sys.stdin.readline().strip().split()
    A, B = int(_l[0]), int(_l[1])

    if B not in graph[A]:
        graph[A].append(B)
    
    if A not in graph[B]:
        graph[B].append(A)

bacon = []
for c in range(1, N+1):
    dist = [0 if i == c else 9999999 for i in range(N+1)]
    
    visited = [False] * (N+1)
    visited[0] = True
    q = deque()

    current = graph[c]
    level = 1
    while len(current) != 0:
        next = []
        for i in current:
            if visited[i] == False:
                dist[i] = level
                visited[i] = True
                next.extend(graph[i])

        level += 1
        current = next

    bacon.append(sum(dist[1:]))
#for i in bacon:
#    print(i)
print(bacon.index(min(bacon))+1)    