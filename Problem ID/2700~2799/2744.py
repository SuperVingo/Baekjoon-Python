l = input()
t = ""

for i in l:
    if i.isupper():
        t = t + i.lower()
    elif i.islower():
        t = t + i.upper()
    else:
        t = t + i
print(t)