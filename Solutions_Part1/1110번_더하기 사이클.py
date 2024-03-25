n=int(input())
l=[]; cnt=0
if n<10:
    l.append(0)
    l.append(n)
else:
    l.append(n//10)
    l.append(n%10)

l.append((l[0]+l[1])%10)
cnt+=1

while 1:
    if l[1]*10+l[2] == n : break
    l[0]=l[1]; l[1]=l[2]; l[2]=((l[0]+l[1])%10)
    cnt+=1
print(cnt)
