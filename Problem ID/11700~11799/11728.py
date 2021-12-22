n = input().split()
a = int(n[0])
b = int(n[1])
lst = []
line = input().split()
for i in range(a):
    lst.append(int(line[i]))
line = input().split()
for i in range(b):
    lst.append(int(line[i]))
lst.sort()
for i in range(len(lst) - 1):
    print(lst[i], end=' ')
print(lst[len(lst)-1])