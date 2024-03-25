import sys
lines=[sys.stdin.readline().rstrip('\n') for _ in range(int(input()))]
for i in lines:
    stack=[]
    for j in i :
        if j=='(' : stack.append(j)
        elif j==')' :
            if stack != [] : stack.pop()
            elif stack == [] : stack.append(000); break
    if stack==[] : print('YES')
    else : print('NO')
