alpha='abcdefghijklmnopqrstuvwxyz'
alpha_2='ABCDEFGHIJKLMNOPQRSTUVWXYZ'
n=input().lower()
cnt_list=[]

for i in range(26):
    cnt_list.append(0)
for i in n:
    cnt_list[alpha.index(i)]+=1

if cnt_list.count(max(cnt_list))>1:
    print('?')
else :
    print(alpha_2[cnt_list.index(max(cnt_list))])
