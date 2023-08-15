from sys import stdin

N, B = stdin.readline().split()
B = int(B)
ilenn = len(N)
iresult = 0
for i in N:
    try:
        inum = int(i)
    except:
        inum = 10 + ord(i) - ord('A')
    iresult += inum * (B ** (ilenn-1))
    ilenn -= 1

print(iresult)