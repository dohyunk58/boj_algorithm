from sys import stdin

lCroatia = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']

sstr = stdin.readline().rstrip()
ilen_sstr = len(sstr)

for i in lCroatia:
    if i in sstr:
        ilen_sstr -= sstr.count(i)

print(ilen_sstr)
