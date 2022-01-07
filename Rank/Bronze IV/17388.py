line = input().split()
s = int(line[0])
g = int(line[1])
h = int(line[2])

if(s + g + h >= 100):
    print('OK')
else:
    if(s == min(s, g, h)):
        print('Soongsil')
    elif(g == min(s, g, h)):
        print("Korea")
    else:
        print('Hanyang')