n=int(input())
odd=['*',' ']; even=[' ','*']
temp_1=''; temp_2=''
for j in range(n):temp_1+=odd[j%2]
for j in range(n):temp_2+=even[j%2]
for j in range(n):
    print(temp_1)
    print(temp_2)
