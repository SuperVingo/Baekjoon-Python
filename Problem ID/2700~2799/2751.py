import sys
n = int(sys.stdin.readline().strip())

lst = []
for i in range(n):
    lst.append(int(sys.stdin.readline().strip()))

lst.sort()
for i in lst:
    sys.stdout.write(str(i) + '\n')