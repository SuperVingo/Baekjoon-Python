line = input().split()
a = int(line[0]) * 1000
b = int(line[1]) * 1000
lst = [b*7, (b // 2) * 7, (b // 4) * 7]
lst.sort(reverse=True)
print(lst)
for i in lst:
    if(a >= i):
        print(i)
        exit(0)
print(0)
