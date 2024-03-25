cts=0; msts=0
temp=input().split(':')
temp=list(map(int, temp))
cts += temp[2]+60*temp[1]+3600*temp[0]

temp=input().split(':')
temp=list(map(int, temp))
msts += temp[2]+60*temp[1]+3600*temp[0]

result_list=[]
result=msts-cts

result_list.append(result%60)
result//=60

result_list.append(result%60)
result//=60
if result<0 : result=24+result

result_list.append(result)

for i in range(1,4):
    if result_list[-i]<10:
        result_list[-i]='0'+str(result_list[-i])
    else : result_list[-i]=str(result_list[-i])

print('%s:%s:%s'%(result_list[2], result_list[1], result_list[0]))
