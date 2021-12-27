import math
a = int(input())
b = int(input())
c = int(input())
d = int(input())
e = int(input())

i = math.ceil(b/d)
j = math.ceil(c/e)
print(a-max(i, j))