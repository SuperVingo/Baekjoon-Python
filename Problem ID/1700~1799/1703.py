while(True):
    line = input().split()
    if(line[0] == '0'):
        break
    s = 1
    for i in range(1, len(line), 2):
        s = s * int(line[i]) - int(line[i+1])
    print(s)