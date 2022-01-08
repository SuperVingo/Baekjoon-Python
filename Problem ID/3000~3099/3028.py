line = input()
a = 1
for i in line:
    if(i == 'A'):
        if(a == 1):
            a = 2
        elif(a == 2):
            a = 1
    elif(i == 'B'):
        if(a == 2):
            a = 3
        elif(a == 3):
            a = 2
    else:
        if(a == 1):
            a = 3
        elif(a == 3):
            a = 1
print(a)