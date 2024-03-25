n=int(input())
for i in range(n):
    if i==0:
        print(' '*(n-1)+'*')
    elif 1<=i<n-1:
        print(' '*(n-i-1)+'*'+' '*(2*i-1)+'*')
    else :
        print('*'*(2*n-1))
