# 입력받은 문자열의 알파벳이 몇 번째 칸에 있는지 리스트에 저장 후 출력
import sys
alpha_list = [-1]*123  # 알파벳 소문자 아스키코드 97 ~ 122를 위한 배열 생성
S = sys.stdin.readline().rstrip()  # rstrip으로 개행문자 제거
setS = set(S)  # 문자열 중복 제거
for i in range(len(setS)):
    alpha_list[ord(list(setS)[i])] = S.index(
        list(setS)[i])  # 해당 알파벳이 입력받은 문자열의 몇 번째에 있는지 저장
print(*alpha_list[97:123])
