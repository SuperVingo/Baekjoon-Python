t1 = input().split(":")
t2 = input().split(":")

t1_sec = int(t1[0]) * 3600 + int(t1[1]) * 60 + int(t1[2])
t2_sec = int(t2[0]) * 3600 + int(t2[1]) * 60 + int(t2[2])

if(t1_sec >= t2_sec):
    t2_sec = t2_sec + 24 * 3600

time = t2_sec - t1_sec
print("%02d:%02d:%02d" % (time//3600, (time%3600)//60, time%60))