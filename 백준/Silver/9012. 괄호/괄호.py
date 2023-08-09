from sys import stdin

inum = int(stdin.readline())

for i in range(inum):
    stack_vps = []
    str = stdin.readline().rstrip()
    for j in list(str):
        if j == '(':
            stack_vps.append('C')
        elif j == ')':
            if len(stack_vps) == 0:
                stack_vps.append(')')
                break
            else:
                stack_vps.pop()
    if len(stack_vps) != 0:
        print('NO')
    else:
        print('YES')