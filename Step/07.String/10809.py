line = input()
lst = [-1] * 26
for i in range(len(line)):
    if(lst[ord(line[i]) - ord('a')] != -1):
        continue
    lst[ord(line[i]) - ord('a')] = i
for i in lst:
    print(i, end=' ')