line = input().split()
a = int(line[0])
b = int(line[1])
if(a == 0 and b == 0):
    print('Not a moose')
elif(a == b):
    print('Even', a*2)
else:
    print('Odd', max(a, b)*2)