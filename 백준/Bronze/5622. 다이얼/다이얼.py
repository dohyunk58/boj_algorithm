from sys import stdin

numcount = 0  # 다이얼 이동 시간 카운트 (1=2초, 2=3초 ... 9=10초)
sstr = stdin.readline().rstrip()

for i in sstr:
    if i < "S":
        numcount += int((ord(i)-59)/3+1)  # ord('A') = 65, (65-59)/3 = 2
    elif i < "Z":
        numcount += int((ord(i)-60)/3+1)  # 7이 PQRS 4개이기 때문
    else:
        numcount += 10  # 문자가 Z인경우

print(numcount)
