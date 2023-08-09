from sys import stdin

def find_index(list, findnum):
    for i in range(len(list)):
        findlist = list[i]
        try:
            indextwo = findlist.index(findnum)
            indexone = i
        except:
            continue
    print(indexone+1, indextwo+1)


numlist = [0]*9
maxnum = [0]*9
for i in range(9):
    numlist[i] = list(map(int, stdin.readline().split()))
    maxnum[i] = max(numlist[i])

print(max(maxnum))
find_index(numlist, max(maxnum))