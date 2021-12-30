line = input().split()
a = int(line[0])
b = int(line[1])
c = int(line[2])
d = int(line[3])

t = (a*c)%(b*d*2)
if(t == 0):
    print(1)
else:
    print(0)