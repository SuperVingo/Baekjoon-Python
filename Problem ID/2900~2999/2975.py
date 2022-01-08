while True:
    line = input().split()
    if(line[0] == '0' and line[2] == '0'):
        break

    if(line[1] == 'W'):
        if(int(line[0]) - int(line[2]) < -200):
            print('Not allowed')
        else:
            print(int(line[0]) - int(line[2]))
    else:
        print(int(line[0]) + int(line[2]))