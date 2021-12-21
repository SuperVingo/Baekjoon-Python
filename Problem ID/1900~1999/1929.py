lst = [True] * 1000000
lst[0] = False
lst[1] = False

for i in range(2, 1001):
    for j in range(i*2, 1000000, i):
        lst[j] = False

line = input().split()
a = int(line[0])
b = int(line[1])
for i in range(a, b+1):
    if(lst[i]):
        print(i)