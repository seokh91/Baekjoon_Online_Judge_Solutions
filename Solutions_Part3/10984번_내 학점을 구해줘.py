l=[]
n=int(input())
for i in range(n):
    l.append([])
    n_1=int(input())
    for _ in range(n_1):
        a,b=input().split()
        a=int(a); b=float(b)
        l[i].append((a,b))

for i in range(n):
    result_1=0; result_2=0.0
    for j in range(len(l[i])):
        result_1+=l[i][j][0]
        result_2+=l[i][j][1]*l[i][j][0]
    print('%d %.1f'%(result_1, result_2/result_1))
