word=input()
result_l=[]
cnt=0; ten=''

for i in word:
    cnt+=1; ten+=i
    if cnt==10:
        cnt=0
        result_l.append(ten)
        ten=''
result_l.append(ten)

for i in result_l:
    print(i)
