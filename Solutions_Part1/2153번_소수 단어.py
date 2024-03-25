import sys
import math
line=sys.stdin.readline()
s='abcdefghijklmnopqrstuvwxyz'
b='ABCDEFGHIJKLMNOPQRSTUVWXYZ'

def is_prime(num):
    if num==1 or num==2 or num==3 :return True
    elif num%2==0 : return False
    for i in range(3, int(math.sqrt(num))+1):
        if num%i==0: return False
    return True

temp_num=0
for i in line:
    if i in s:
        temp_num += (s.index(i)+1)
    elif i in b:
        temp_num += (b.index(i)+27)

if is_prime(temp_num):
    print('It is a prime word.')
else:
    print('It is not a prime word.')
