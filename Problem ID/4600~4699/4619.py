while True:
    line = list(map(int, input().split()))
    if(line[0] == 0 and line[1] == 0):
        break

    n = 0
    for i in range(1, line[0]+1):
        if(line[0] <= i**line[1]):
            n = i-1
            break
    if(abs(n**line[1] - line[0]) > abs((n+1)**line[1] - line[0])):
        print(n+1)
    else:
        print(n)
