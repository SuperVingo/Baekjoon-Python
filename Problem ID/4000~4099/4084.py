while True:
    line = list(map(int, input().split()))
    if(line[0] == 0 and line[1] == 0 and line[2] == 0 and line[3] == 0):
        break

    cnt = 0
    while True:
        if(line[0] == line[1] and line[1] == line[2] and line[2] == line[3]):
            break

        t = [abs(line[0]-line[1]), abs(line[1]-line[2]), abs(line[2]-line[3]), abs(line[3]-line[0])]
        cnt += 1
        line = t
    print(cnt)