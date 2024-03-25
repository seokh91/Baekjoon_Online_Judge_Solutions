import sys
import math

def is_prime(num):
    if num == 1 : return False
    if num == 2 or num ==3 : return True
    elif num % 2 == 0 : return False
    max_=math.sqrt(num)
    for i in range(3, int(max_)+1):
        if num%i==0 : return False
    return True
    
l=list(map(int, sys.stdin.readline().split()))
for i in range(l[0], l[1]+1):
    if is_prime(i) : print(i)
