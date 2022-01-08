import math
line = input().split()
a = int(line[0])
b = int(line[1])

if(a == 0 or b == 0):
    print('Impossible')
elif(a == 1 or b == 1):
    print('1')
elif(a == b):
    print(int(math.sqrt(a+b)))
else:
    print(int(math.sqrt(min(a, b)* 2 + 1)))

