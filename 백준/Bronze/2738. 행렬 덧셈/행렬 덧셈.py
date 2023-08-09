from sys import stdin

N, M = map(int, stdin.readline().split())

sline_one = [list(map(int, stdin.readline().split())) for _ in range(N)]
sline_two = [list(map(int, stdin.readline().split())) for _ in range(N)]

for i in range(N):
    for j in range(M):
        sline_one[i][j] += sline_two[i][j]
for i in sline_one:
    print(*i)