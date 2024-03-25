import sys
n=int(input()) ; temp=[i for i in range(1, n+2)] ; judge=False ; judge_2=False
operations=[] ; stack=[] ; seq=[]
for i in range(1, n+1):
    seq.append(int(sys.stdin.readline().rstrip('\n')))

for se in seq:
    while se >= temp[0] :
        stack.append(temp[0]) ; operations.append('+') ; temp.pop(0)
        if se == stack[len(stack)-1] :
            stack.pop() ; operations.append('-') ; judge_2=True ; break

    if judge_2 : judge_2=False ; continue

    if se < temp[0] :
        if stack[len(stack)-1] == se :
            stack.pop() ; operations.append('-')
        else :
            judge=True ; print('NO') ; break

if not judge :
    for i in operations : print(i)
