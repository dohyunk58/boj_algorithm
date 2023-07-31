from sys import stdin
sstr = stdin.readline().rstrip().lstrip()  # rstrip과 lstrip은 공백 기준 우측, 좌측 제거
if sstr == '':
    print(0)
else:
    print(sstr.count(' ')+1)
