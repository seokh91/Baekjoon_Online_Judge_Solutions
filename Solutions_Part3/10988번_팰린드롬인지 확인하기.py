word=input()
word_list=list(word)

judge=0
for i in range(len(word_list)//2):
    if word_list[i] != word_list[len(word_list)-1-i]:
        print(0)
        break
    else :
        judge+=1
if judge==(len(word_list)//2): print(1)
