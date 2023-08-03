from sys import stdin
sstr = stdin.readline().rstrip()
sstr = sstr.upper() # 입력받은 문자열 대문자로 변경
set_sstr = set(sstr) # 입력받은 문자열에 있는 알파벳 set 생성
biggest = '?' # 기본값 ?
count = 0
for i in set_sstr:
    if count < sstr.count(i): # 더 많은 알파벳의 경우
        count = sstr.count(i)
        biggest = i
    elif count == sstr.count(i): # 같은 수를 가진 알파벳이 있는 경우
        count = sstr.count(i)
        biggest = '?'
print(biggest)