from sys import stdin

inum = int(stdin.readline())
meetings = sorted([list(map(int, stdin.readline().split())) for _ in range(inum)], key = lambda x : (x[1], x[0])) # key 인자에 앞부분이 우선순위를 가
count = 1
end = meetings[0][1]
del meetings[0]
while len(meetings) != 0:
    try:
        if meetings[0][0] < end: # 시작 시간 < 끝나는 시간
            del meetings[0]
        else: # 시작 시간 >= 끝나는 시간
            count +=1
            end = meetings[0][1]
            del meetings[0]
    except:
        break
print(count)