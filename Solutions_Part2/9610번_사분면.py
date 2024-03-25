n=int(input())
l=[]
for i in range(n):
    a,b=input().split()
    a=int(a); b=int(b)
    l.append((a,b))

q1=0; q2=0; q3=0; q4=0; axis=0

for i in range(n):
    if l[i][0]==0 or l[i][1]==0: axis+=1
    elif l[i][0]>0 and l[i][1]>0: q1+=1
    elif l[i][0]<0 and l[i][1]>0: q2+=1
    elif l[i][0]<0 and l[i][1]<0: q3+=1
    else : q4+=1

print('Q1: %d\nQ2: %d\nQ3: %d\nQ4: %d\nAXIS: %d'%(q1,q2,q3,q4,axis))
