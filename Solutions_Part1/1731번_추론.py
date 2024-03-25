import sys
l=[] ; judge=0
for _ in range(int(input())):
    l.append(int(sys.stdin.readline().rstrip('\n')))

if l[1]-l[0] == l[2]-l[1] : judge=1

if judge==1 : print(l[len(l)-1]+l[1]-l[0])
else : print(l[len(l)-1]*(l[1]//l[0]))
