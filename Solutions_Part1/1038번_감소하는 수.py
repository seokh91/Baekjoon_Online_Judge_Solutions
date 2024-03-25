def next_decre(num, cnt, N):

    if cnt==N : print(num) ; return
    
    temp=list(str(num)) ; flag=False
    for i in range(-1,-len(temp),-1):
        if int(temp[i-1])-int(temp[i]) >= 2 :
            flag=True
            temp[i]=str(int(temp[i])+1) ; last=i ; break
        
    if not flag :
        last=-len(temp)
        temp[last]=str(int(temp[last])+1)

    rest=0
    for j in range(-1, last, -1):
        temp[j]=str(rest) ; rest+=1

    return next_decre(int(''.join(temp)), cnt+1, N)
        
if __name__=="__main__":

    N=int(input())
    ranges=[9,54,174,384,636,846,966,1011,1021,1022]
    mi=[0,0,10,210,3210,43210,543210,6543210,76543210,876543210,9876543210]

    if N>=1023 : print(-1)
    elif N<=9 : print(N)
    else :
        radix=0 ; cnt=0
        for i in range(10):
            if N<=ranges[i] : radix=i+1 ; cnt=ranges[i-1]+1 ; break
            
        next_decre(mi[radix], cnt, N)
