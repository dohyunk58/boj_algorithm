from sys import stdin

iperson = int(stdin.readline())
ltime = list(map(int, stdin.readline().split()))
ltime.sort()
itotal_time = 0

for i in range(iperson):
    itotal_time += ltime[i]*(iperson-i)
print(itotal_time)