from sys import stdin

count = 0  # 다이얼 이동 시간 카운트 (1=2초, 2=3초 ... 9=10초)

ddial = {'A': 2, 'B': 2, 'C': 2,
         'D': 3, 'E': 3, 'F': 3,
         'G': 4, 'H': 4, 'I': 4,
         'J': 5, 'K': 5, 'L': 5,
         'M': 6, 'N': 6, 'O': 6,
         'P': 7, 'Q': 7, 'R': 7, 'S': 7,
         'T': 8, 'U': 8, 'V': 8,
         'W': 9, 'X': 9, 'Y': 9, 'Z': 9}  # 주어진 알파벳을 숫자로 대응(딕셔너리)

lstr = list(stdin.readline().rstrip())  # 문자열을 한 글자씩 리스트로 만들기

for i in lstr:
    # print(i)
    # print(ddial[i])
    count += ddial[i]+1

print(count)
