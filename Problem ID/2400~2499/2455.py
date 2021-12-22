lst = []
cnt = 0
for i in range(4):
    line = input().split()
    cnt = cnt + int(line[1]) - int(line[0])
    lst.append(cnt)
print(max(lst))