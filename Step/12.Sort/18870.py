import sys

n = int(input())
lst = []
line = sys.stdin.readline().strip().split()
for i in range(n):
    lst.append(int(line[i]))
sr = sorted(list(set(lst)))
dict = {}
for i in range(len(sr)):
    dict[sr[i]] = i

for i in range(n - 1):
    sys.stdout.write(str(dict[lst[i]]) + ' ')
sys.stdout.write(str(sr.index(lst[len(lst) - 1])))