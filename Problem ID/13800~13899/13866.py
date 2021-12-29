line = input().split()
a = int(line[0])
b = int(line[1])
c = int(line[2])
d = int(line[3])
ls = [a,b,c,d]
ls.sort()
print(abs((ls[0] + ls[3]) - (ls[1] + ls[2])))