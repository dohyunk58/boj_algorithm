from sys import stdin
inum = int(stdin.readline())
for i in range(inum):
    irepeatnum, sstr = stdin.readline().split()
    for j in sstr:
        print(j*int(irepeatnum), end='')
    print('')