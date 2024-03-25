import sys

def make(x, y):

    if y<=0 and -x>=y and x>=y :
        return 4*abs(y)**2-abs(y)+1-x
    elif y>0 and -y<=x and y>=x :
        return x+4*abs(y)**2+3*abs(y)+1
    elif x>0 and x>-y and x>y :
        return 4*abs(x)**2-3*abs(x)+1-y
    else :
        return 4*abs(x)**2+abs(x)+1+y

r1,c1,r2,c2=list(map(int, sys.stdin.readline().rstrip().split()))
res=[[0 for _ in range(c2-c1+1)] for _ in range(r2-r1+1)] ; m_list=[]

for i in range(r2-r1+1):
    for j in range(c2-c1+1):
        res[i][j]=make(j+c1,i+r1)
    m_list.append(max(res[i]))

m=len(str(max(m_list)))
for i in res:
    for j in i :
        tmp=len(str(j))
        if tmp==m : print(str(j), end=" ")
        else :
            print(' '*(m-tmp)+str(j), end=" ")
    print()
