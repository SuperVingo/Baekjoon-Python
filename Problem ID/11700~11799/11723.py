import sys

s = set()

n = int(sys.stdin.readline().strip())
for i in range(n):
    l = sys.stdin.readline().strip().split()
    

    if l[0] == "add":
        v = int(l[1])
        s.add(v)
    elif l[0] == "remove":
        v = int(l[1])
        s.remove(v)
    elif l[0] == "check":
        v = int(l[1])
        if v in s:
            print(1)
        else:
            print(0)
    elif l[0] == "toggle":
        v = int(l[1])
        if v in s:
            s.remove(v)
        else:
            s.add(v)
    elif l[0] == "all":
        s.clear()
        for c in range(1, 21):
            s.add(c)
    elif l[0] == "empty":
        s.clear()
