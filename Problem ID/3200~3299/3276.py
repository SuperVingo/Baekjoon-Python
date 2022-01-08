import math
a = int(input())
l = int(math.floor(math.sqrt(a)))
h = int(math.ceil(math.sqrt(a)))
if(l*h < a):
    print(l+1, h)
else:
    print(l, h)