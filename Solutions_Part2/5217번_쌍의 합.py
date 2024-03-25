for _ in range(int(input())):
    n=int(input()) ; result=[]

    if n%2==0 :
        for i in range(1,n//2):
            result.append(str(i)+' '+str(n-i))
        print('Pairs for',str(n)+':',', '.join(result)) ; result.clear()
    else :
        for i in range(1,n//2+1):
            result.append(str(i)+' '+str(n-i))
        print('Pairs for',str(n)+':',', '.join(result)) ; result.clear()
