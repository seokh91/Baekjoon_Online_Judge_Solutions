x=int(input())
l=[64]

while x != sum(l) :
    if x < sum(l) :
        temp=l.pop(); l.append(temp//2)
    elif x > sum(l) :
        l.append(l[len(l)-1]//2)

print(len(l))
