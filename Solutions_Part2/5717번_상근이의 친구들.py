l=[]
while True:
    a,b=input().split()
    a=int(a); b=int(b)
    if a==0 and b==0: break
    l.append((a,b))

for i in range(len(l)):
    print(sum(l[i]))
