n, m = map(int, input().split())
l = list(map(int, input().split()))

start = 1
end = max(l)
while True:
    mid = (start + end) // 2

    t = 0
    for i in l:
        t = t + max(0, i - mid)
    
    if t >= m:
        start = mid
    else:
        end = mid
    
    if abs(start - end) <= 1:
        break
print((start + end) // 2)
