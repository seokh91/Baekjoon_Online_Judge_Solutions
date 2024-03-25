row=[list(map(int, input().split())) for _ in range(9)]
temp=max(row[0]); temp_index=0
for i in range(1, 9):
    if temp < max(row[i]) :
        temp=max(row[i]); temp_index=i
print(temp)
print(temp_index+1, (row[temp_index].index(temp))+1)
