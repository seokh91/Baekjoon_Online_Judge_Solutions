import sys
lines=[]; n=int(input())
for _ in range(n):
    get=sys.stdin.readline().split()
    temp=''
    for i in get[::-1]:
        temp+=i; temp+=' '
    lines.append(temp)
for i in range(n):
    print('Case #%d: %s'%(i+1, lines[i]))
