line = input().split()
l = int(line[0])
n = int(line[1])

line = input().split()
for i in range(l):
    if(n > int(line[i])):
        print(int(line[i]), end=' ')