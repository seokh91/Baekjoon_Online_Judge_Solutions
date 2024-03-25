import sys
n=int(input())
l=[list(map(int, sys.stdin.readline().split())) for _ in range(n)]
for i in range(n):
    l[i]=l[i][1:l[i][0]+1]
    l[i].sort(reverse=True)

def find_min(temp):
    max_=(temp[0]-temp[1])
    for i in range(1, len(temp)-1):
        if max_<(temp[i]-temp[i+1]):max_=(temp[i]-temp[i+1])
    return max_       
    
for i in range(n):
    print('Class %d'%(i+1))
    print('Max %d, Min %d, Largest gap %d'%(max(l[i]), min(l[i]), find_min(l[i])))
