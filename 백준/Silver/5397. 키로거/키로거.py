from sys import stdin

# 스택을 사용해서 문제를 풀기

# 스택을 2개 만들어서 ABCD를 순서대로 넣음, 다른 빈 스택에는 < 가 입력되었을 떄 기존 스택에서 pop으로 가져옴
# > 명령일 때에는 우측 스택에서 pop으로 가져옴

N = int(stdin.readline())

for _ in range(N):
    sstr = stdin.readline().rstrip()
    front_stack = []
    back_stack = []
    answer = []

    for i in sstr:
        if i == '<':
            if front_stack:
                back_stack.append(front_stack.pop())
        elif i == '>':
            if back_stack:
                front_stack.append(back_stack.pop())
        elif i == '-':
            if front_stack:
                front_stack.pop()
        else:
            front_stack.append(i)

    print("".join(front_stack),"".join(back_stack[::-1]),sep='')
        

