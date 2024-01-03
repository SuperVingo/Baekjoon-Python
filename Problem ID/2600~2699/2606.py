import sys

N = int(sys.stdin.readline())
M = int(sys.stdin.readline())

graph = []
for i in range(N+1):
    graph.append([])

for i in range(M):
    A, B = map(int, sys.stdin.readline().split())
    graph[A].append(B)
    graph[B].append(A)

stack = []
stack.extend(graph[1])
visited = [False] * (N+1)
visited[1] = True
while len(stack) != 0:
    c = stack.pop()
    visited[c] = True
    for i in graph[c]:
        if not visited[i]:
            stack.append(i)

c = 0
for i in visited:
    if i:
        c += 1
print(c-1)