for i in range(3):
    line = input().split()
    h = int(line[0])
    m = int(line[1])
    s = int(line[2])
    t1 = h * 3600 + m * 60 + s
    h = int(line[3])
    m = int(line[4])
    s = int(line[5])
    t2 = h * 3600 + m * 60 + s
    h = (t2-t1) // 3600
    m = ((t2-t1) % 3600) // 60
    s = (t2-t1) % 60
    print(h, m, s)