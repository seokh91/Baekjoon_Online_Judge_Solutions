result_list=[]
for _ in range(int(input())):
    h,w,n=map(int, input().split())
    temp=list(divmod(n, h))
    if temp[1]==0: temp[1]=h; temp[0]-=1
    result=(temp[1]*100+temp[0]+1)
    result_list.append(result)
    
for i in result_list:
    print(i)
