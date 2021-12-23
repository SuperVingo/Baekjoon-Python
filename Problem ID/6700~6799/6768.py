n = int(input())
cnt = 0
for i in range(1, n-2):
    for j in range(i+1, n-1):
        for k in range(j+1, n):
            cnt += 1
print(cnt)