n = int(input())
line = input().split()
s = 0
c = 1
for i in line:
    if i == '1':
        s += c
        c += 1
    else:
        c = 1
print(s)