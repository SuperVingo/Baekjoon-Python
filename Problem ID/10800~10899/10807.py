line = int(input())
lst = list(map(int, input().split()))
n = int(input())
cnt = 0
for i in lst:
    if n == i:
        cnt = cnt + 1
print(cnt)