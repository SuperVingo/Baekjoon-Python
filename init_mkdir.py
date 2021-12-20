import os

num = 1000
path = "F:/Baekjoon-Solved/"

for i in range(229):
    filename = str(num) + "~" + str(num + 99)
    os.mkdir(path + filename)
    num = num + 100