x,y,w,h=map(int, input().split())
l=[h-y, x, y, w-x]
print(min(l))
