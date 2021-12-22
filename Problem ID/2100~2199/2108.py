import sys

cnt = [0] * 8001
n = int(sys.stdin.readline().strip())
lst = []
for i in range(n):
    t = int(sys.stdin.readline().strip())
    lst.append(t)
    cnt[t+4000] += 1
lst.sort()

if(len(lst) == 1):
    print(lst[0])
    print(lst[0])
    print(lst[0])
    print(0)
else:
    print(int(round(sum(lst) / len(lst), 0)))
    print(lst[int(len(lst) / 2)])
    m = max(cnt)
    most = []
    for i in range(len(cnt)):
        if(cnt[i] == m):
            most.append(i)
    if(len(most) == 1):
        print(most[0] - 4000)
    else:
        print(most[1] - 4000)
    print(max(lst) - min(lst))