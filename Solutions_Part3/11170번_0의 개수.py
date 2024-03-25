n=int(input())
result_l=[]
for _ in range(n):
    a,b=input().split()
    cnt=0
    for i in range(int(a),int(b)+1):
        temp=list(str(i))
        cnt+=temp.count('0')
    result_l.append(cnt)
    temp.clear()
for i in result_l:
    print(i)
