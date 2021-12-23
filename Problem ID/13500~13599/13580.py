line = input().split()
a = int(line[0])
b = int(line[1])
c = int(line[2])
if(a == b or b == c or a == c or a == b+c or b == a+c or c == a+b):
    print('S')
else:
    print('N')
    