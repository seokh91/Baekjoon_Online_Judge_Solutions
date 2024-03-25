n=int(input())
fibo=[0,1]
if n==0: print(0)
elif n==1: print(1)
else :
    for i in range(2, n+1):
        fibo.append(fibo[i-1]+fibo[i-2])
    print(fibo[n])
