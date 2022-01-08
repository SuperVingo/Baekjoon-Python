line = list(map(int, input().split()))
print(max(abs(line[0] - line[1]), abs(line[1] - line[2])) - 1)