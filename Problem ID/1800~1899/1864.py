while(True):
    line = input()
    if(line == '#'):
        break
    s = 0
    for i in range(len(line)):
        if(line[i] == '\\'):
            s += 8**(len(line) - i - 1)
        elif(line[i] == '('):
            s += (8**(len(line) - i - 1))*2
        elif(line[i] == '@'):
            s += (8**(len(line) - i - 1))*3
        elif(line[i] == '?'):
            s += (8**(len(line) - i - 1))*4
        elif(line[i] == '>'):
            s += (8**(len(line) - i - 1))*5
        elif(line[i] == '&'):
            s += (8**(len(line) - i - 1))*6
        elif(line[i] == '%'):
            s += (8**(len(line) - i - 1))*7
        elif(line[i] == '/'):
            s += (8**(len(line) - i - 1))*(-1)
    print(s)