n = int(input())
for z in range(n):
    line = input().split()
    num = int(line[0])
    str = line[1]
    for i in str:
        for j in range(num):
            print(i, end='')
    print()
