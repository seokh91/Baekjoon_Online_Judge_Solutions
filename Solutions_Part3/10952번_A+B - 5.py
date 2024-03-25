l=[]
while True :
    a,b=input().split()
    a=int(a); b=int(b)
    if a==0 and b==0: break
    else: l.append(a+b)

for i in range(len(l)):
    print(l[i])
