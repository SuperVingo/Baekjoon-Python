while True:
    line = list(map(int, input().split()))
    if(line[0] == 0 and line[1] == 0 and line[2] == 0 and line[3] == 0):
        break

    print(str(int(min(max(min(line[2]/line[0], line[3]/line[1]), min(line[3]/line[0], line[2]/line[1]))*100, 100)))+'%')
