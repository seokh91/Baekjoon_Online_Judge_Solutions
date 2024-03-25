l=[]; l_1=[]
for _ in range(10001):
    l.append(0)
for i in range(10001):
    l_1.append(i)

def self_num(num):
    result=num
    for i in list(str(num)):
        result+=int(i)
    return result

for i in l_1[1:]:
    temp=self_num(i)
    if temp <= 10000: l[temp]=1
for i in l_1[1:]:
    if l[i]==0:
        print(i)
