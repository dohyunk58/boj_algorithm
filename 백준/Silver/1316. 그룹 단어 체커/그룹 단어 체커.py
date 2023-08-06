from sys import stdin

igroup_count = 0
inum = int(stdin.readline())
for l in range(inum):
    sstr = stdin.readline().strip()
    setS = list(set(sstr))
    bgroup_flag = True  # 그룹여부 플래그

    for i in setS:
        if sstr.count(i) == 1:
            continue  # 1개만 있는 알파벳 통과
        start_loc = sstr.index(i)  # 알파벳의 첫번째 위치
        end_loc = start_loc
        for j in range(start_loc, len(sstr)):  # 알파벳 그룹의 맨 앞과 맨 뒤 확인
            try:
                if sstr[j+1] == sstr[j]:
                    continue
                else:
                    end_loc = j  # 알파벳 마지막 위치
                    break
            except: # baa와 같이 마지막인 경우
                end_loc = j
                break
        for k in range(end_loc+1, len(sstr)):  # 마지막 위치+1 이후부터 확인
            if sstr[k] == i:
                bgroup_flag = False

    if bgroup_flag == True:
        igroup_count += 1

print(igroup_count)