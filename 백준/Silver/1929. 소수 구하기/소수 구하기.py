import math
import sys
input = sys.stdin.readline

def primenumber(x):
    for i in range(2, int(math.sqrt(x))+1):
        if x % i == 0:
            return False
    return True

start, end = map(int, input().split())
if start == 1:
    start += 1

for i in range(start, end+1):
    if primenumber(i) == True:
        print(i)