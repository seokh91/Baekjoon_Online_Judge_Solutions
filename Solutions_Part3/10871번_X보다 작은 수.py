import sys
length, num=sys.stdin.readline().split()
length=int(length); num=int(num)
elements=list(map(int,sys.stdin.readline().split()))

result=[]
for i in range(length):
    if elements[i] < num : result.append(elements[i])

for i in range(len(result)):
    print(result[i], end=' ')
