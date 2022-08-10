import sys

graph_list = []          

def dfs(x, y, m, n):
    if x < 0 or y < 0 or x >= m or y >= n:
        return False
    elif graph_list[y][x] == 1:
        graph_list[y][x] = 0
        dfs(x+1, y, m, n)
        dfs(x-1, y, m, n)
        dfs(x, y+1, m, n)
        dfs(x, y-1, m, n)
        return True
    return False

T = int(sys.stdin.readline().strip())
for _ in range(T):
    count = 0
    m, n, k = map(int, sys.stdin.readline().strip().split())
    graph_list = [[0 for i in range(m)] for j in range(n)]

    for _1 in range(k):
        x, y = map(int, sys.stdin.readline().strip().split())
        graph_list[y][x] = 1
    
    for y in range(n):
        for x in range(m):
            if dfs(x, y, m, n):
                count += 1
    print(count)
    
