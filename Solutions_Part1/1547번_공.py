import sys
l=[1,2,3]
for _ in range(int(input())):
    a,b=list(map(int, sys.stdin.readline().rstrip('\n').split()))
    tmp_1=l.index(a) ; tmp_2=l.index(b)
    temp=l[tmp_1] ; l[tmp_1]=l[tmp_2] ; l[tmp_2]=temp
print(l[0])
