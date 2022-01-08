lst = []
line = input().split()
a = int(line[0])
b = int(line[1])
lst.append(a/b)

n = int(input())
for i in range(n):
    line = input().split()
    a = int(line[0])
    b = int(line[1])
    lst.append(a/b)
print("%.2f" % (min(lst)*1000))