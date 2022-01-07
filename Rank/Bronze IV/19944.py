line = input().split()
n = int(line[0])
m = int(line[1])
if(m <= 2):
    print('NEWBIE!')
elif(m <= n):
    print('OLDBIE!')
else:
    print('TLE!')