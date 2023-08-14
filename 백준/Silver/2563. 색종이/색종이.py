from sys import stdin

rowlen = 100
columnlen = 100

table = []
for _ in range(rowlen):
    table.append([0 for _ in range(columnlen)])

N = int(stdin.readline())
for _ in range(N):
    row, column = map(int, stdin.readline().split())
    for i in range(row,row+10):
        for j in range(column,column+10):
            table[i][j] = 1

count = 0

for i in range(rowlen):
    for j in range(columnlen):
        if table[i][j] == 1:
            count += 1
            
print(count)