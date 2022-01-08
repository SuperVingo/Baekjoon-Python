line = input().split()
n = int(line[0])
k = int(line[1])
lst = []
for i in range(1, n+1):
    if(n % i == 0):
        lst.append(i)
if(len(lst) > k - 1):
    print(lst[k-1])
else:
    print(0)