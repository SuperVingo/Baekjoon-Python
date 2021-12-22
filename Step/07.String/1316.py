n = int(input())
cnt = 0
for z in range(n):
    lst = [False] * 26
    line = input()
    result = line[0]
    for i in range(1, len(line)):
        if(line[i - 1] != line[i]):
            result = result + line[i]
    line = result
    fail = False
    for i in line:
        if(not lst[ord(i) - ord('a')]):
            lst[ord(i) - ord('a')] = True
        else:
            fail = True
            break

    if(not fail):
        cnt = cnt + 1
print(cnt)