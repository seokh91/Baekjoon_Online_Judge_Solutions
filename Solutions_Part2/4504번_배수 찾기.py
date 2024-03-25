import sys
n=int(input())
while True:
    temp=int(sys.stdin.readline().rstrip('\n'))
    if temp == 0 : break
    else :
        if temp % n == 0 : print('%d is a multiple of %d.'%(temp, n))
        else : print('%d is NOT a multiple of %d.'%(temp,n))
