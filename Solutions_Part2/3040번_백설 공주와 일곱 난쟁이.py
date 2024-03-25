import sys
l=[int(sys.stdin.readline()) for _ in range(9)]
l.sort()
for i in range(8):
    for j in range(i+1, 9):
        if (sum(l)-l[i]-l[j]) == 100 :
            l[i]=0; l[j]=0
            break
for i in l:
    if i!=0: print(i)
