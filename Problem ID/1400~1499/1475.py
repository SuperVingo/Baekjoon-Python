from math import floor
import sys
import math

N = sys.stdin.readline().strip()

c = [0] * 10
for i in N:
    c[int(i)] += 1

m = max(c[:6] + c[7:9] + [math.ceil((c[6] + c[9]) / 2)])

print(m)