import sys
t=tuple(int(x) for x in sys.stdin.readline().rstrip('\n').split())

if t[2]-t[1] > t[1]-t[0] : print(t[2]-t[1]-1)
else : print(t[1]-t[0]-1)
