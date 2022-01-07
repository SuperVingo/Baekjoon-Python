line = input().split()
x = int(line[0])
y = int(line[1])
z = int(line[2])
line = input().split()
sx = int(line[0])
sy = int(line[1])
sz = int(line[2])

if(z <= sz):
    if(y <= sy):
        if(x <= sx):
            print('A')
        elif(x / 2 <= sx):
            print('B')
        else:
            print('C')
    elif(y / 2 <= sy):
        print('D')
    else:
        print('E')
else:
    print('E')
