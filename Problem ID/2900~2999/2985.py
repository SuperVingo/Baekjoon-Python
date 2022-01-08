line = list(map(int, input().split()))
if(line[0] + line[1] == line[2]):
    print("%d%c%d%c%d" % (line[0], '+', line[1], '=', line[2]))
elif(line[0] - line[1] == line[2]):
    print("%d%c%d%c%d" % (line[0], '-', line[1], '=', line[2]))
elif(line[0] * line[1] == line[2]):
    print("%d%c%d%c%d" % (line[0], '*', line[1], '=', line[2]))
elif(line[0] // line[1] == line[2]):
    print("%d%c%d%c%d" % (line[0], '/', line[1], '=', line[2]))
elif(line[0] == line[1] + line[2]):
    print("%d%c%d%c%d" % (line[0], '=', line[1], '+', line[2]))
elif(line[0] == line[1] - line[2]):
    print("%d%c%d%c%d" % (line[0], '=', line[1], '-', line[2]))
elif(line[0] == line[1] * line[2]):
    print("%d%c%d%c%d" % (line[0], '=', line[1], '*', line[2]))
elif(line[0] == line[1] // line[2]):
    print("%d%c%d%c%d" % (line[0], '=', line[1], '/', line[2]))