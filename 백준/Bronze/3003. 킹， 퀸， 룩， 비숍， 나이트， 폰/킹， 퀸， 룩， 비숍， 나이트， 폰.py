from sys import stdin

lchess = [1, 1, 2, 2, 2, 8]  # 정상적인 체스 말 개수
linput = list(map(int, stdin.readline().split()))  # 입력받는 체스 말 개수
lchange = [0]*6  # 변화량 리스트

for i in range(6):
    lchange[i] = lchess[i]-linput[i]

print(*lchange)
