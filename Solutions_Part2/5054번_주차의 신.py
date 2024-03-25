import sys
n=int(input())
l=[]
for _ in range(n):
    temp=int(input())
    a=list(map(int, sys.stdin.readline().split()))
    l.append(sorted(a))

for i in l:
    temp_list=[]
    if len(i)==1 : print(0)
    else :
        for j in range(len(i)-1
                       ):
            temp_list.append(i[j+1]-i[j])
        print(2*sum(temp_list))
