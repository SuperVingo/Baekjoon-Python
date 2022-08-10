import sys

k, n = map(int, input().split())
l = []
for i in range(k):
    l.append(int(sys.stdin.readline().strip()))

start = 1
end = max(l)
mid = (start + end) // 2
while True:
    mid = (start + end) // 2
    print(start, mid, end)
    t = 0
    for j in l:
        t = t + (j // mid)
    if t < n:
        end = mid
    elif t >= n:
        start = mid
    
    if end - start <= 1:
        break

t = 0
for j in l:
    t = t + (j // end)
    print(t)
if t == n:
    print(end)
else:
    print((start + end) // 2)