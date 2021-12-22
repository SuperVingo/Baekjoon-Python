import math

n = int(input())

for _ in range(n):
    line = input().split()
    x = int(line[0])
    y = int(line[1])
    
    leng = y - x
    sq = math.sqrt(leng)
    down = (math.floor(sq))**2
    up = (math.ceil(sq))**2

    #print(leng, sq, down, up)

    if(up - leng > leng - down):
        print(int(math.sqrt(down) * 2))
    else:
        print(int(math.sqrt(up) * 2) - 1)
