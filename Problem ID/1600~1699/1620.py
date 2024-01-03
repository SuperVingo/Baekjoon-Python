import sys

N, M = map(int, sys.stdin.readline().strip().split())

poke = []
for i in range(N):
    poke.append(sys.stdin.readline().strip())

for i in range(M):
    prob = sys.stdin.readline().strip()

    if prob.isdigit():
        print(poke[int(prob)-1])
    else:
        print(poke.index(prob)+1)