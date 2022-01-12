while True:
    line = list(map(int, input().split()))
    if(line[0] == 0 and line[1] == 0):
        break

    if(line[0] > line[1]):
        print('Yes')
    else:
        print('No')