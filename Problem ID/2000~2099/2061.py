line = input().split()
p = int(line[0])
k = int(line[1])

lst = [True] * 1000001
for i in range(2, 1001):
    for j in range(i*2, 1000001, i):
        lst[j] = False
lst[2] = True

for i in range(2, k):
    if(p % i == 0):
        print('BAD ' + str(i))
        exit(0)
print('GOOD')