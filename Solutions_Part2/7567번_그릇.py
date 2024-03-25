dish=input()
dish_list=list(dish)
length=10

for i in range(len(dish_list)-1):
    if dish_list[i]==dish_list[i+1]:
        length+=5
    else : length+=10

print(length)
