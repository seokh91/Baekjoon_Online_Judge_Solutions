char=['c=','c-','dz=','d-','lj','nj','s=','z=']
alpha='abcdefghijklmnopqrstuvwxyz'
n=list(input())
for _ in range(3):
    n.append('')
cnt=0

for i in range(len(n)-3):
    if n[i]=='c' and (n[i+1]=='=' or n[i+1]=='-') :
        n[i]=''; n[i+1]=''
        cnt+=1
    elif n[i]=='d' and ((n[i+1]=='z' and n[i+2]=='=') or n[i+1]=='-') :
        if n[i+1]=='z' and n[i+2]=='=' :
            n[i]=''; n[i+1]=''; n[i+2]=''
        elif n[i+1]=='-':
            n[i]=''; n[i+1]=''
        cnt+=1
    elif n[i]=='l' and n[i+1]=='j' :
        n[i]=''; n[i+1]=''
        cnt+=1
    elif n[i]=='n' and n[i+1]=='j' :
        n[i]=''; n[i+1]=''
        cnt+=1
    elif n[i]=='s' and n[i+1]=='=' :
        n[i]=''; n[i+1]=''
        cnt+=1
    elif n[i]=='z' and (n[i+1]=='=' and n[i-1]!='d') :
        n[i]=''; n[i+1]=''
        cnt+=1
    elif n[i]!='' and n[i] in alpha :
        cnt+=1
print(cnt)
