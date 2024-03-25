import sys
n=int(input())
l=[]
for _ in range(n):
    l.append(int(sys.stdin.readline().rstrip('\n')))

l.sort(reverse=True) ; flag=False

for a in range(1, len(l)):
    if l[a]*3 
    if flag : break
    for b in range(a, len(l)):
        if flag : break
        for c in range(b, len(l)):
            if l[a]+l[b]+l[c] in l : print(l[a]+l[b]+l[c]) ; flag=True ; break
