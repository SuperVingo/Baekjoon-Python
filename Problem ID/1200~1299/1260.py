import sys
from collections import deque

N, M, V = map(int, sys.stdin.readline().strip().split())
graph = [[] for i in range(N+1)]

for i in range(M):
    s, d = map(int, sys.stdin.readline().strip().split())
    graph[s].append(d)
    graph[d].append(s)

for i in range(len(graph)):
    graph[i].sort()

visited = [False] * (N+1)
def dfs(graph, V):
    visited[V] = True
    print(V, end=' ')
    for i in graph[V]:
        if not visited[i]:
            dfs(graph, i)
dfs(graph, V)
print()

visited = [False] * (N+1)
def bfs(graph, s):
    queue = deque([s])
    visited[s] = True
    while queue:
        v = queue.popleft()
        print(v, end=' ')
        for i in graph[v]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True
bfs(graph, V)