n=list(input())
temp=[]
for _ in range(len(n)):
    max_num=n[0]
    for j in range(len(n)):
        if max_num<n[j]: max_num=n[j]
    temp.append(max_num)
    n.remove(max_num)

result=''
for i in temp:
    result+=i
print(int(result))
