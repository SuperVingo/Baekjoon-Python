line = input().lower()

lst = [0] * 26
for i in line:
    lst[ord(i) - ord('a')] = lst[ord(i) - ord('a')] + 1

m = max(lst)
cnt = 0
for i in lst:
    if(m == i):
        cnt = cnt + 1
if(cnt > 1):
    print("?")
else:
    print(chr(lst.index(max(lst)) + 65))
