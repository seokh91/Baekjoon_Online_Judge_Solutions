l=[]
n=int(input())

for _ in range(n):
    r,e,c = input().split()
    l.append((int(r),int(e)-int(c)))

for i in range(len(l)):
    if l[i][0]<l[i][1]: print('advertise')
    elif l[i][0]==l[i][1]: print('does not matter')
    else : print('do not advertise')
