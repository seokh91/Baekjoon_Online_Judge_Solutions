n=int(input())
result=0
def func(i):
    result=0
    for j in range(i+1):
        result+=j
    return result

for i in range(1,n+1):
    result+=(func(i)+i*(i+1))

print(result)
