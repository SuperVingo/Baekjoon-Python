line = input()
if(len(line) == 2):
    print(int(line[0]) + int(line[1]))
else:
    if(line[1] == '0'):
        print(int(line[:2]) + int(line[2:]))
    else:
        print(int(line[0]) + int(line[1:]))

