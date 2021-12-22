lst = [True] * 10000
lst[0] = False
lst[1] = False

for i in range(2, 101):
    for j in range(i*2, 10000, i):
        lst[j] = False

n = int(input())
for _ in range(n):
    num = int(input())
    half = num // 2
    if(lst[half]):
        print(half, half)
    else:
        up = 0
        down = 0
        for j in range(half, 10000):
            if(lst[j]):
                up = j
                break
        for j in range(half, 0, -1):
            if(lst[j]):
                down = j
                break
        while(True):
            if(up + down > num):
                for j in range(down - 1, 0, -1):
                    if(lst[j]):
                        down = j
                        break
            elif(up + down < num):
                for j in range(up+1, 10000):
                    if(lst[j]):
                        up = j
                        break
            else:
                print(down, up)
                break