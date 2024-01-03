import sys

N, M = map(int, sys.stdin.readline().strip().split())

hear = []
for i in range(N):
    hear.append(sys.stdin.readline().strip())

see = []
for i in range(M):
    see.append(sys.stdin.readline().strip())

hearsee = sorted(set(hear).intersection(see))
print(len(hearsee))
for i in hearsee:
    print(i)