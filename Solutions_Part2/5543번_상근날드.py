import sys
hamburger=[int(sys.stdin.readline()) for _ in range(3)]
bever=[int(sys.stdin.readline()) for _ in range(2)]

price_set=min(hamburger)+min(bever)-50
print(price_set)
