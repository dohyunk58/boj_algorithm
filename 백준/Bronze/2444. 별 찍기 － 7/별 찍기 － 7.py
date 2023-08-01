from sys import stdin

istar = int(stdin.readline())

for i in range(1, istar+1):
    print(" "*(istar-i)+"*"*(2*i-1))
for i in range(istar-1, 0, -1):
    print(" "*(istar-i)+"*"*(2*i-1))