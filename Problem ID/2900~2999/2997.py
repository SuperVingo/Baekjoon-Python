line = sorted(list(map(int, input().split())))
if(abs(line[0] - line[1]) == abs(line[1] - line[2])):
    print(line[2] + abs(line[0] - line[1]))
elif(abs(line[0] - line[1]) == abs(line[1] - line[2]) * 2):
    print(line[0] + (abs(line[0] - line[1])//2))
else:
    print(line[1] + (abs(line[2] - line[1])//2))