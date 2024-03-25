import sys
n=int(input())
l=[int(sys.stdin.readline()) for _ in range(n)]

for i in l :
    if i==0:
        print(1, 0)
    elif i==1:
        print(0, 1)
    else:
        cnt_0=[1,0]; cnt_1=[0,1]
        for j in range(2, i+1):
            cnt_0.append(cnt_0[j-1]+cnt_0[j-2])
            cnt_1.append(cnt_1[j-1]+cnt_1[j-2])
        print(cnt_0[len(cnt_0)-1], cnt_1[len(cnt_1)-1])
