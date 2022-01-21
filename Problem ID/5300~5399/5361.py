n = int(input())
for i in range(n):
    lst = list(map(int, input().split()))
    print("$%.2f" % (lst[0]*350.34 + lst[1]*230.90 + lst[2]*190.55 + lst[3]*125.30 + lst[4]*180.90))