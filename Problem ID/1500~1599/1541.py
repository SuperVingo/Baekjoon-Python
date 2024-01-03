import sys

line = sys.stdin.readline().strip().split('-') 
lst = []

for l in line:
    lst.append(sum(list(map(int, l.split('+')))))

print(int(lst[0]) - int(sum(lst[1:])))    