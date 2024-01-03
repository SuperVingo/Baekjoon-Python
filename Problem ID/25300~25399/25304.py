import sys

X = int(sys.stdin.readline())
N = int(sys.stdin.readline())
cost = 0
for i in range(N):
    A, B = map(int, sys.stdin.readline().split())
    cost += A*B
if X == cost:
    print('Yes')
else:
    print('No')