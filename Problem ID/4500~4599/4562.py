n = int(input())
for i in range(n):
    line = list(map(int, input().split()))
    if(line[0] < line[1]):
        print('NO BRAINS')
    else:
        print('MMM BRAINS')