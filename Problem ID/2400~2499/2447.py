import sys

n3 = int(input())
plane = [[' '] * n3 for i in range(n3)]

def printstar(n: int, sx: int, sy: int):
    if(n == 1):
        return

    for _ in range(0, n):
        plane[sy][sx+_] = '*'
        plane[sy+_][sx] = '*'
        plane[sy+n-1][sx+_] = '*'
        plane[sy+_][sx+n-1] = '*'

    printstar(n // 3, sx, sy)
    printstar(n // 3, sx + (n // 3), sy)
    printstar(n // 3, sx + (n // 3) * 2, sy)
    printstar(n // 3, sx + (n // 3) * 2, sy + (n // 3) * 1)
    printstar(n // 3, sx + (n // 3) * 2, sy + (n // 3) * 2)
    printstar(n // 3, sx + (n // 3) * 1, sy + (n // 3) * 2)
    printstar(n // 3, sx, sy + (n // 3) * 2)
    printstar(n // 3, sx, sy + (n // 3) * 1)

printstar(n3, 0, 0)
for i in plane[:n3]:
    for j in i[:n3]:
        sys.stdout.write(j)
    sys.stdout.write("\n")