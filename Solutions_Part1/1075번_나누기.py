n=int(input())
f=int(input())
n=int(str(n//100)+'00')

while True:
    if n%f==0:
        print(str(n)[-2]+str(n)[-1]); break
    n+=1
