line = input().split()
a = int(line[0])
b = int(line[1])
if(a % 2 == 0 or b % 2 == 0):
    print(0)
else:
    print(min(a, b))