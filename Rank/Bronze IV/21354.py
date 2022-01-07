line = input().split()
a = int(line[0])
b = int(line[1])
if(a*7 < b*13):
    print('Petra')
elif(a*7 > b*13):
    print('Axel')
else:
    print('lika')
