line = input().split()
a = int(line[0])
b = int(line[1])
c = int(line[2])
print((a+b+c) - min(a, b, c) - max(a, b, c))