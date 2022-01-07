line = input().split()
a = int(line[0])
b = int(line[1])
c = int(line[2])
d = int(line[3])
if(c <= a-2 and d <= b-2):
    print(1)
else:
    print(0)