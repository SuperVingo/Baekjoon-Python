n = int(input())
lst = [ [] for x in range(200)]
for i in range(n):
    line = input().split()
    age = int(line[0])
    name = line[1]
    lst[age - 1].append(name)

for i in range(200):
    if(len(lst[i]) != 0):
        for j in range(len(lst[i])):
            print(i+1, lst[i][j])