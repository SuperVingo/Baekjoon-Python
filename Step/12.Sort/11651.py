n = int(input())

lst = []
for i in range(n):
    line = input().split()
    lst.append((int(line[0]), int(line[1])))

f = sorted(lst, key=lambda x : (x[1], x[0]))
for i in f:
    print(i[0], i[1])