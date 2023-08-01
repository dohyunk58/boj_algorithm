import sys

lstr = [] 
while True:
    sinput = sys.stdin.readline().rstrip()
    if sinput == '': # 빈칸일 경우 입력 종료
        break
    else:
        lstr.append(sinput)

for i in lstr:
    print(i)
