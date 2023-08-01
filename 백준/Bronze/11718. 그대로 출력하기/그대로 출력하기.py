import sys

lstr = []
while True:
    sinput = sys.stdin.readline().rstrip()
    if sinput == '':
        break
    else:
        lstr.append(sinput)

for i in lstr:
    print(i)