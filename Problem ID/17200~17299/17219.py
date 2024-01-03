import sys

N, M = map(int, sys.stdin.readline().split())

dic = {}
for i in range(N):
    S, P = sys.stdin.readline().split()
    dic[S] = P

for i in range(M):
    S = sys.stdin.readline().strip()
    print(dic[S])
    