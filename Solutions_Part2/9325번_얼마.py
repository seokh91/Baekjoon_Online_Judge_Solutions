n=int(input()); result_list=[]
for _ in range(n):
    sol=0
    price=int(input())
    sol+=price
    num_option=int(input())
    for _ in range(num_option):
        a,b=input().split()
        a=int(a); b=int(b)
        if a==0 : break
        sol+=a*b
    result_list.append(sol)

for i in range(len(result_list)):
    print(result_list[i])
