line = input().split()
a = int(line[0])
b = int(line[1])
if((abs(a-b)+1) % 2 == 0):
    print((a+b)*((abs(a-b)+1) // 2))
else:
    print((a+b)*((abs(a-b)+1) // 2) + (a+b)//2)
