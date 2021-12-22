lst = []
for i in range(9):
    line = input().split()
    t = []
    for j in range(9):
        t.append(int(line[j]))
    lst.append(t)
r = 0
c = 0
m = 0
for i in range(9):
    if(m < max(lst[i])):
        m = max(lst[i])
        r = i + 1
        c = lst[i].index(max(lst[i])) + 1
print(m)
print(r, c)