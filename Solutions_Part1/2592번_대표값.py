import sys
l=[int(sys.stdin.readline()) for _ in range(10)]
avg=int(sum(l)/len(l))

dic={}
for i in range(10):
    dic.setdefault(l[i], l.count(l[i]))

most=max(dic, key=dic.__getitem__)

print(avg)
print(most)
