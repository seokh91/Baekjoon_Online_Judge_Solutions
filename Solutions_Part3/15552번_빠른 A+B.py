import sys

for _ in range(int(sys.stdin.readline().rstrip())):
    print(sum(list(map(int, sys.stdin.readline().rstrip().split()))))
