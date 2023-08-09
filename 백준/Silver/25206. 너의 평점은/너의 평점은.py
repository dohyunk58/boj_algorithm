from sys import stdin

# 전공평점 = ( 전공과목 학점 x 과목평점 ) / 학점 총합
dscore = {'A+':4.5, 'A0':4.0, 'B+':3.5, 'B0':3.0, 'C+':2.5, 'C0':2.0, 'D+':1.5, 'D0':1.0, 'F':0.0}
ftotal = 0.0
fcredit = 0

# P/F 과목 중 P는 계산에서(학점 총합에서도) 제외
for i in range(20): # 20개의 과목
    score = list(stdin.readline().rstrip().split())
    if score[2] == 'P':
        continue
    else:
        ftotal += float(score[1]) * dscore[score[2]]
        fcredit += float(score[1])
print(ftotal/fcredit)