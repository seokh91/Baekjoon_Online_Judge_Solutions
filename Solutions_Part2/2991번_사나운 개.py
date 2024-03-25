a,b,c,d=map(int, input().split())
p,m,n=map(int, input().split())
dog_1=[0]; dog_2=[0]
dog_1+=([1]*a+[0]*b)*(1000)
dog_2+=([1]*c+[0]*d)*(1000)
for i in (p,m,n):
    print(dog_1[i]+dog_2[i])
