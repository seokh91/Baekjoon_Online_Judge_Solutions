l=[]
while True:
    sentence=input()
    if sentence=='END': break
    else: l.append(sentence)
for i in l:
    result=''
    for j in range(1, len(i)+1):
        result+=i[-j]
    print(result)
