import sys
l=list(map(int, sys.stdin.readline().split()))

if l[0]==1:
    cnt=0
    for i in range(1, 9):
        if i!=l[i-1]:
            print('mixed')
            break
        else : cnt+=1
    if cnt==8:
        print('ascending')

elif l[0]==8:
    cnt=0
    for i in range(8, 0, -1):
        if i!=l[8-i]:
            print('mixed')
            break
        else : cnt+=1
    if cnt==8:
        print('descending')

else : print('mixed')
