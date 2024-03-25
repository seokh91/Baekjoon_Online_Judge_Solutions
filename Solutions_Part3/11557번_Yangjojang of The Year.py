T=int(input()); win_l=[]
for _ in range(T):
    N=int(input())
    for i in range(N):
        if i==0:
            a,b=input().split()
            b=int(b); winner=(a,b)
        else:
            a,b=input().split()
            b=int(b)
            if winner[1] < b : winner=(a,b)
    win_l.append(winner[0])

for i in range(T):
    print(win_l[i])
