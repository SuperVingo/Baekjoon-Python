line = input().split()
n = int(line[0])
w = int(line[1])
h = int(line[2])

ml = w**2 + h**2

for i in range(n):
    a = int(input())
    if(a**2 <= ml):
        print('DA')
    else:
        print('NE')