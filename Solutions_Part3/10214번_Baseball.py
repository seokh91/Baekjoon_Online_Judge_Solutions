dic={}
T=int(input())
for i in range(1,T+1):
    yp=0; kp=0
    for _ in range(9):
        a,b=input().split()
        a=int(a); b=int(b)
        yp+=a; kp+=b
    if yp>kp: dic.setdefault(i,'Yonsei')
    elif yp<kp: dic.setdefault(i,'Korea')
    else: dic.setdefault(i,'Draw')

for i in range(1,T+1):
    print(dic[i])
