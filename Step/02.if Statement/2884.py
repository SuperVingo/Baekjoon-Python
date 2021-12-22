time = input().split()
hour = int(time[0])
min = int(time[1])

if(min >= 45):
    min = min - 45
else:
    hour = hour - 1
    min = min + 15

if(hour < 0):
    hour = hour + 24

print(hour, min)