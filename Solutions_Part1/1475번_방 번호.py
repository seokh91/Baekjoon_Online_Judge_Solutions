n=input(); int_n=list(map(int, n))
check=[0]*9; cnt=temp=0;
for i in int_n:
    if i==9 and cnt==0 : temp=int_n.count(9); cnt+=1
    elif i!=9 and check[i]==0 : check[i]=int_n.count(i)
check[6]+=temp

if check[6]%2==0 : num_69=check[6]//2
else : num_69=check[6]//2; num_69+=1
check[6]=num_69

print(max(check))
