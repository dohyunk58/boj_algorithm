from sys import stdin
inum = int(stdin.readline())
for i in range(inum):
    slist = []
    irepeatnum, sstr = stdin.readline().split()
    for j in sstr:
        for k in range(int(irepeatnum)):
            slist.append(j)
    print(*slist, sep='')
