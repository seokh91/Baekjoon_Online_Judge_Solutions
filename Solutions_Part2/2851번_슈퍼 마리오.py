l=[]; score=0
for _ in range(10):
    score += int(input())
    l.append((abs(100-score), score))
l.sort(); temp=[]; key=l[0][0]
for i in range(10):
    if l[i][0]==key : temp.append(l[i])
temp.sort(reverse=True)
print(temp[0][1])
