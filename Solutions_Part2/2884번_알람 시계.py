import sys
r=lambda:sys.stdin.readline()
h,m=map(int, r().split())

total_min=60*h+m-45

new_m=total_min%60
new_h=(total_min//60)%24

print(new_h, new_m)
