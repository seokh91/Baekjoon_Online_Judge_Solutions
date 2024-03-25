import sys
from collections import Counter
card_num=Counter()
for _ in range(int(input())):
    card_num[int(sys.stdin.readline())]+=1
card_num=card_num.most_common()
temp=card_num[0][1]; temp_min=card_num[0][0]
for i in card_num:
    if i[1] != temp : break
    if i[0] < temp_min : temp_min=i[0]
print(temp_min)
