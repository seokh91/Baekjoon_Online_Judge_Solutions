import sys

for _ in range(int(input())):
    n=int(input()) ; cnt=0 ; stack=[]
    ary=list(map(int, sys.stdin.readline().rstrip('\n').split())) ; ary=[0]+ary

    for i in range(1, len(ary)):
        if ary[i] != 'a' :
            stack.append((i, ary[i]))
            while stack != [] :
                tmp=stack.pop() ; begin=i
                if begin == tmp[1] :
                    cnt+=1
                else :
                    stack.append((tmp[1], ary[tmp[1]]))
                ary[tmp[0]]='a'

    print(cnt)
