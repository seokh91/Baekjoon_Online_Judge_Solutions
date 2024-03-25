l=[]
a,b,c=input().split()
l.append(int(a)); l.append(int(b)); l.append(int(c))

dic={1:0, 2:0, 3:0, 4:0, 5:0, 6:0}

for i in range(3):
    dic[l[i]] += 1

dic_values=list(dic.values())

for i in range(len(dic_values)):
    if dic_values[i]!=0:
        if dic_values[i]==3:
            judge=1; index=i+1; break
        elif dic_values[i]==2:
            judge=2; index=i+1; break
        else: judge=3; index=i+1

if judge==1:
    result = 10000+index*1000
    print(result)
elif judge==2:
    result = 1000+index*100
    print(result)
elif judge==3:
    result = 100*index
    print(result)
