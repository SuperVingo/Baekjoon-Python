n = int(input())
for _ in range(n):
    lst = []
    a = list(map(int, input().split()))
    for i in a:
        if(i % 2 == 0):
            lst.append(i)
    if(len(lst) == 0):
        print(-1)
    else:
        print(sum(lst), min(lst))