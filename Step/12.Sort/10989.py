import sys
cnt = [[i, 0] for i in range(1, 10001)]

n = int(sys.stdin.readline().strip())
for i in range(n):
    cnt[int(sys.stdin.readline().strip()) - 1][1] += 1

str = ''
for i in range(10000):
    for j in range(cnt[i][1]):
        print(i+1)