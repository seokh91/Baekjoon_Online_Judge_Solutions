import sys
word=sys.stdin.readline().rstrip('\n')
for i in range(2, len(word)+1):
    temp_l=[]
    for j in range(i):
        element=word[j:j+len(word)-i+1]
        temp_l.append(element)
        if temp_l.count(element)>=2:
            print(len(element))
            break
    if temp_l.count(element)>=2:
        break
