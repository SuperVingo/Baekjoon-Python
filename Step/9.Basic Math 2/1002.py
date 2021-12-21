import math
def getDist(x1:int, y1:int, x2:int, y2:int):
    return (abs(x1-x2) ** 2 + abs(y1-y2) ** 2)

n = int(input())
for _ in range(n):
    line = input().split()
    x1 = int(line[0])
    y1 = int(line[1])
    r1 = int(line[2])
    x2 = int(line[3])
    y2 = int(line[4])
    r2 = int(line[5])

    if(x1 == x2 and y1 == y2):
        if(r1 != r2):
            print(0)
        else:
            print(-1)
    else:
        d = getDist(x1, y1, x2, y2)
        if(d > (r1 + r2) ** 2 or d < (abs(r1 - r2)) ** 2):
            print(0)
        elif(d == (r1 + r2) ** 2 or d == (abs(r1 - r2)) ** 2):
            print(1) 
        elif(d < (r1 + r2) ** 2 or d > (abs(r1 - r2)) ** 2):
            print(2)
