from operator import itemgetter

n = int(input())

lst = []
for _ in range(n):
    line = input().split()
    lst.append([int(line[0]), int(line[1]), 0, _])

for i in range(n):
    for j in range(n):
        if(i == j):
            continue
        if(lst[i][0] < lst[j][0] and lst[i][1] < lst[j][1]):
            lst[i][2] += 1

for i in lst[:-1]:
    print(i[2] + 1, end=' ')
print(lst[len(lst) - 1][2] + 1)