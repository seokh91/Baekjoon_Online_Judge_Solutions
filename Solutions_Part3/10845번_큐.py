import sys
queue=[]
for _ in range(int(input())):
    order=sys.stdin.readline().split()
    if 'push' == order[0] : queue.append(int(order[1]))
    elif 'pop' == order[0] :
        if queue == [] : print(-1)
        elif queue != [] : print(queue.pop(0))
    elif 'size' == order[0] : print(len(queue))
    elif 'empty' == order[0] :
        if queue == [] : print(1)
        elif queue != [] : print(0)
    elif 'front' == order[0] :
        if queue == [] : print(-1)
        elif queue != [] : print(queue[0])
    elif 'back' == order[0] :
        if queue == [] : print(-1)
        elif queue != [] : print(queue[len(queue)-1])
