import sys
n = int(sys.stdin.readline().strip())
s = 0
for i in range(n):
    s += int(sys.stdin.readline().strip())
print(s - (n-1))