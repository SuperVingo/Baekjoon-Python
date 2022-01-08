i = 1
while True:
    line = input().split()
    if(line[1] == '0'):
        break

    print("Trip #%d: %.2f %.2f" % (i,(float(line[0])/63360)*3.1415927*float(line[1]), (float(line[0])/63360)*3.1415927*float(line[1]) * (3600/float(line[2]))))
    i += 1