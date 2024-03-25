import sys
stack=[]
for _ in range(int(input())):
    order=sys.stdin.readline().split()
    if 'push' == order[0] :
        stack.append(int(order[1]))
    elif 'top' == order[0] :
        if stack==[] : print(-1)
        else : print(stack[len(stack)-1])
    elif 'size' == order[0] :
        print(len(stack))
    elif 'empty' == order[0] :
        if stack == [] : print(1)
        else : print(0)
    elif 'pop' == order[0] :
        if stack==[] : print(-1)
        else : print(stack.pop(len(stack)-1))
