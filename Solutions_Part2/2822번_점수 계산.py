import sys
score=[int(sys.stdin.readline()) for _ in range(8)]
sorted_score=sorted(score)
result=0; index_list=[]
for i in range(1, 6):
    result+=sorted_score[-i]
    index_list.append(score.index(sorted_score[-i])+1)
index_list.sort()
print(result)
for i in index_list:
    print(i, end=' ')
