import sys

N = int(sys.stdin.readline().strip())

c2 = 0
c5 = 0
c10 = 0
for i in range(2, N+1):
    while True:
        if i % 10 == 0:
            c10 += 1
            i = i // 10
            continue
        elif i % 5 == 0:
            c5 += 1
            i = i // 5
            continue
        elif i % 2 == 0:
            c2 += 1
            i = i // 2
            continue
        else:
            break

print(c10 + min(c2, c5))