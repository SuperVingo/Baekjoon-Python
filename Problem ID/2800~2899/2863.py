st = input().split(" ")
a = int(st[0])
b = int(st[1])
st = input().split(" ")
c = int(st[0])
d = int(st[1])

lst = []
lst.append(a/c + b/d)
lst.append(c/d + a/b)
lst.append(d/b + c/a)
lst.append(b/a + d/c)
if(max(lst) == lst[0]):
    print('0')
elif(max(lst) == lst[1]):
    print('1')
elif(max(lst) == lst[2]):
    print('2')
else:
    print('3')