from sys import stdin
sstr = stdin.readline().rstrip()
iblankcount = 0
if len(sstr) > 0:
    if sstr[0] == ' ':  # 맨 앞 공백 카운트
        iblankcount += 1
    if sstr[-1] == ' ':  # 맨 뒤 공백 카운트
        iblankcount += 1
    if sstr == ' ':
        iblankcount += 1  # 빈칸만 존재하는 경우 0 + 1 - 1로 만들어줌
    print(sstr.count(' ')+1-iblankcount)
else:
    print(0)