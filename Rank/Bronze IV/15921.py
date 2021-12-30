n = int(input())
if(n == 0):
    print('divide by zero')
    exit(0)

lst = []
line = input().split()
for n in line:
    lst.append(int(n))

lst.sort()

avg = sum(lst) / len(lst)

ex = 0
v = lst[0]
cnt = 1
for i in lst[1:]:
    if(i == v):
        cnt += 1
    else:
        ex += (v * (cnt / len(lst)))
        v = i
        cnt = 1
ex += (v * (cnt / len(lst)))

print("%.2f" % (avg/ex))