import sys

N = int(sys.stdin.readline())
lst = list(map(int, sys.stdin.readline().split()))
X = int(sys.stdin.readline())

c = 0
for i in range(len(lst)):
    for j in range(i + 1, len(lst) + 1):
        if lst[i] + lst[j] == X:
