
from sys import stdin

table = [list(stdin.readline().rstrip()) for _ in range(5)]
str = ''
maxlen = 0

for i in range(5):
    maxlen = len(table[i]) if maxlen < len(table[i]) else maxlen

for j in range(maxlen):
    for i in range(5):
        try:
            str += table[i][j]
        except:
            continue

print(str)
