import sys
l=list(sys.stdin.readline().split())
temp_list=[]
for i in range(2):
    temp=''
    temp+=(l[i][2]+l[i][1]+l[i][0])
    temp_list.append(int(temp))

print(max(temp_list))
