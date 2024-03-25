l=[]
while True:
    a,b=input().split()
    a=int(a); b=int(b)    
    if a==0 and b==0: break
    l.append((a,b))

for i in range(len(l)):
    if l[i][0]%l[i][1]==0: print('multiple')
    elif l[i][1]%l[i][0]==0: print('factor')
    else : print('neither')
    
      
