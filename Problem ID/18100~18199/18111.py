import sys

n, m, b = map(int, sys.stdin.readline().strip().split())
maps = [list(map(int, sys.stdin.readline().strip().split())) for i in range(n)]

cost = []
start = min(min(maps))
end = max(max(maps))

for i in range(start, end+1):
    t = 0
    u = 0
    for y in range(n):
        for x in range(m):
            a = i - maps[y][x]
            
            if a > 0:
                t = t + a
            elif a < 0:
                t = t + -a * 2

            u = u + a
    if u > b:
        cost.append(999999999)
    else:
        cost.append(t)
print(min(cost), max(list(filter(lambda x: cost[x] == min(cost), range(len(cost)))))+start)
