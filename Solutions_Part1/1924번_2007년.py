l_0=[1,3,5,7,8,10,12]
l_1=[4,6,9,11]
l_2=[2]
yo=['MON', 'TUE', 'WED', 'THU', 'FRI', 'SAT', 'SUN']

month, day=input().split()
month=int(month); day=int(day)
total_day=0

for i in range(1, month+1):
    if month > i :
        if i in l_0: total_day+=31
        elif i in l_1: total_day+=30
        elif i in l_2: total_day+=28
    elif month == i:
        total_day+=(day-1)

total_day%=7
print(yo[total_day])
