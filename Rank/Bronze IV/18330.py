u = int(input())
l = int(input())
cu = l + 60

if(u <= cu):
    print(u*1500)
else:
    print(cu*1500 + abs(u-cu)*3000)