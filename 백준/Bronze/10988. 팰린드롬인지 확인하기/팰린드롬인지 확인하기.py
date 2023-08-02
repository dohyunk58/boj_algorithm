from sys import stdin

sstr = stdin.readline().rstrip()
flag = True
for i in range(len(sstr)//2): # 절반까지 확인
    if sstr[i] != sstr[len(sstr)-i-1]:
        flag = False
print(int(flag))