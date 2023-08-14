from sys import stdin

rowlen = 100
columnlen = 100
table = [[0]*100 for _ in range(100)]
N = int(stdin.readline())

for _ in range(N):
    row, column = map(int, stdin.readline().split())
    for i in range(row,row+10):
        for j in range(column,column+10):
            table[i][j] = 1

count = 0

for i in range(rowlen):
    count += table[i].count(1)

print(count)