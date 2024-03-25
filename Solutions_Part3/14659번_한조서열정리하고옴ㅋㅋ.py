import sys

n=int(input()) ; max_cnt=0
hanjos=tuple(map(int, sys.stdin.readline().rstrip('\n').split()))

for i in range(n):
    cnt=0
    for j in range(i+1, n):
        if hanjos[i] > hanjos[j] : cnt+=1
        else : break
    if cnt > max_cnt : max_cnt=cnt

print(max_cnt)
