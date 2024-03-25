import sys
l=list(map(int, sys.stdin.readline().split()))

sorted_l=[]
for j in range(3):
    min_temp=l[0]
    for i in range(len(l)):
        if l[i]<min_temp: min_temp=l[i]
    sorted_l.append(min_temp)
    l.remove(min_temp)

for i in sorted_l: print(i, end=' ')
